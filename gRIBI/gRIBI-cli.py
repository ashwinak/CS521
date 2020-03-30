#!/usr/bin/env python

# Copyright (C) 2018 Juniper Networks Inc.
#
# Vinay K Nallamothu <nvinay@juniper.net>
# Susan Y. Liu
#
# 2019/02/07 yaliu
#   Revised version
# 2018/06/29 nvinay
#   Initial version

import time, sys, glob
import os
import pdb
import socket
import grpc

sys.path.append("/home/ashwinak/jet/gen/py/")
#sys.path.append("/opt/lib/python2.7/site-packages/jnpr/jet/grpc_services")

import rib_service_pb2
import prpd_service_pb2
import prpd_common_pb2
import jnx_addr_pb2
import authentication_service_pb2
import gribi_service_pb2
import gribi_aft_pb2
import gribi_ywrapper_pb2
import authentication_service_pb2_grpc
import gribi_service_pb2_grpc

#from grpc.beta import implementations
from grpc.framework.interfaces.face.face import *
from prpd_service_pb2 import *
from prpd_common_pb2 import *
from jnx_addr_pb2 import *
from rib_service_pb2 import *
from gribi_service_pb2 import *
from gribi_aft_pb2 import *
from gribi_ywrapper_pb2 import *
from gribi_service_pb2_grpc import *

# Device Details and Login Credentials.
DEFAULT_JSD_HOST        = 'localhost' 
DEFAULT_JSD_GRPC_PORT   = 32767
DEFAULT_JSD_USERNAME    = 'regress'
DEFAULT_JSD_PASSWORD    = 'MaRtInI'

DEFAULT_CLIENT_ID       = 'T_12347'
DEFAULT_APP_COOKIE      = 12345678

# Flags for attributes
ATTR_FLAG_COLOR           = 16

TIMEOUT          = 10      ## Timeout in seconds for an rpc to return back
STREAM_TIMEOUT   = 15      ## Timeout in seconds for streaming API
INFINITE_TIMEOUT = 1000000 ## A large timeout in seconds

## other (future) valid args 'cli', 'stdin', 
progmode        = 'prompt' ## interactive, pause is active
fmt             = 'text' ## IP address and table name format
clientid        = DEFAULT_CLIENT_ID

# For SSL based connections to server
DEFAULT_JSD_SSL_CERTIFICATE_PATH = None

help = """
        gribi-cli.py: gRIBI on JUNOS

        Usage::
        gribi-cli.py -f <cmd-file>

        cmd-file format   
        connect [local|remote <hostname:port>] [noauth] [clientid <client>]
        nhop add table <TABLE> nhid <id> gwaddr <GW-ADDR> intf <IFLNAME>]
             labels <LAB1 LAB2 ...>
        nhgrp add table nhgrpid <NGGRPID-ID> color <COLOR-ID> nhop nhid <ID>
             weight [WEIGHT] ....
        route add table <TABLE> family [inet | inet6] prefix <PREFIX>
             plen <PLEN> nhgrpid <NHGRP-ID.

"""               
def pause():
    global progmode

    if progmode == "prompt":
        programPause = raw_input("Press the <ENTER> key to continue...")

def get_family_from_addr(addr):
    if ':' in addr:
        return 'inet6'
    elif '.' in addr:
        return 'inet'
    elif addr.isdigit():
        return 'mpls'
    else:
        return 'unknown'

def client_metadata(unused_metadata):
    return (('client-id', clientid),)

class label_stack_entry():
    def __init__(self, op, label):
        self.op    = op
        self.label = label

def gribi_get_prefix(pfx, plen, afs, nhid = 0):
    prefix = {}

    if afs == "inet":
        entry = Afts.Ipv4Entry(next_hop_group=UintValue(value=long(nhid)));
        prefix['ipv4'] = Afts.Ipv4EntryKey(prefix=pfx+'/'+str(plen), ipv4_entry=entry)
    elif afs == "inet6":
        entry = Afts.Ipv6Entry(next_hop_group=UintValue(value=long(nhid)));
        prefix['ipv6'] =  Afts.Ipv6EntryKey(prefix=pfx+'/'+str(plen), ipv6_entry=entry)
    elif afs == "mpls":
        entry = Afts.LabelEntry(next_hop_group=UintValue(value=long(nhid)));
        prefix['mpls'] =  Afts.LabelEntryKey(label_uint64=int(pfx), label_entry=entry)
    else:
      print("Unknown family ", afs)

    return prefix

def gribi_build_one_nh(gwaddr, ifl=None, labels=[]):
    print "onenh1"
    if ifl:
        ifd,subunit = ifl.split('.')
    else:
        ifd = ""
        subunit = 0

    print "onenh2"
    intf = Afts.NextHop.InterfaceRef(nh_interface=StringValue(value=ifd),
                                     subinterface=UintValue(value=long(subunit)))

    lblstack = []
    print 30
    for label in labels:
        print "onenh3"
        lblstack.append(Afts.NextHop.PushedMplsLabelStackUnion(pushed_mpls_label_stack_uint64=long(label)))

    return Afts.NextHop(interface_ref=intf, ip_address=StringValue(value=gwaddr), pushed_mpls_label_stack=lblstack)

def gribi_get_nhgrp(nhid, color, nhcnt, gwaddr, weight, bandwidth):
    print 10
    i = 0
    nh = {}
    nhlst = []
    for i in xrange(nhcnt):
        print 11
        onenh = Afts.NextHopGroup.NextHopKey(index=long(gwaddr.get(i)), next_hop=Afts.NextHopGroup.NextHop(weight=UintValue(value=long(weight.get(i, 1)))))
        print 12
        nhlst.append(onenh);

    print 13
    nhg = Afts.NextHopGroupKey(id=nhid, next_hop_group=Afts.NextHopGroup(next_hop=nhlst, color=UintValue(value=color)))

    print 20
    print nhg
    return nhg

def gribi_get_op (op):
    if op in [ "add", "gadd", "nhadd", "nhgadd" ]:
        gop = AFTOperation.ADD
    elif op in [ "update", "upd", "gupd", "nhupd", "nhgupd" ]:
        gop = AFTOperation.REPLACE
    elif op in [ "delete", "del", "gdel", "nhdel", "nhgdel" ]:
        gop = AFTOperation.DELETE
    else:
        gop = AFTOperation.INVALID

    return gop


gribiRequestList = []
gribiOpList = []
opid = 1

def gribi_request_generator():
    global gribiRequestList

    while gribiRequestList:
        req = gribiRequestList.pop(0)
        print("req len", len(req.operation))
        print req
        yield req
    #for req in gribiRequestList:
    #    print("req len", len(req.operation))
    #    print req
    #    yield req

gribi = None

def setup_connection(args):
    global gribi, clientid
    username = DEFAULT_JSD_USERNAME
    password =  DEFAULT_JSD_PASSWORD

    i = 1
    noauth = False
    via_tcp = True

    while i < len(args):
        if args[i] == "local":
            via_tcp = False
        elif args[i] == "remote":
            jet_host,port = args[i+1].split(":")
            jet_port = int(port)
            via_tcp = True
            i = i + 1
        elif args[i] == "user":
            username = args[i+1]
            i = i + 1
        elif args[i] == "password":
            password = args[i+1]
            i = i + 1
        elif args[i] == "clientid":
            clientid = args[i+1]
            i = i + 1
        elif args[i] == "noauth":
            noauth = True
        else:
            print("malformed command: ", args, " at ", args[i])
            return
        i = i + 1

    if via_tcp == False:
        jet_host, jet_port = 'unix:/var/run/japi_rpd', None

    #channel = grpc.insecure_channel(host=jet_host, port=jet_port)
    rtarget = jet_host + ":" + str(jet_port)
    channel = grpc.insecure_channel(target=rtarget)

    if noauth == False:
        login_stub     = authentication_service_pb2_grpc.LoginStub(channel)
        login_request  = authentication_service_pb2.LoginRequest(user_name=username,
                                                       password=password,
                                                       client_id=clientid)
        TIMEOUT = 10
        login_response = login_stub.LoginCheck(login_request, TIMEOUT)
        print(login_response)
        dir(gribi_service_pb2)
        gribi  = gribi_service_pb2_grpc.gRIBIStub(channel)

    else:
        gribi  = gribi_service_pb2.gRIBIStub(channel, metadata_transformer=client_metadata)

def process_route(args):
    global gribiRequestList, gribi, opid
    print("route");

    gop = gribi_get_op(args[1])
    i = 2

    while i < len(args):
        if args[i] in [ "prefix" ]:
            pfx = args[i+1]
            i = i + 1
        elif args[i] in "plen":
            plen = long(args[i+1])
            i = i + 1
        elif args[i] in "family":
            afs = args[i+1]
            i = i + 1
        elif args[i] in [ "nhid", "nhgrpid" ]:
            nhid = args[i+1]
            i = i + 1
        elif args[i] in "table":
            table = args[i+1]
            i = i + 1
        else:
            print("malformed command: ", args, " at ", args[i])
            return

        i = i + 1
    prefix = gribi_get_prefix(pfx, plen, afs, nhid)
    gribiOpList.append(AFTOperation(id=opid, network_instance=table, op=gop, **prefix))
    opid = opid + 1

def process_nexthop(args):
    global gribiRequestList, gribiOpList, opid

    gop = gribi_get_op(args[1])
    i = 2
    label_stack = []
    while i < len(args):
        if args[i] in [ "id", "nhid" ]:
            nhid = long(args[i+1])
            i = i + 1
        elif args[i] in [ "gwaddr", "gateway" ]:
            gwaddr = args[i+1]
            i = i + 1
        elif args[i] in [ "interface", "intf" ]:
            intf = args[i+1]
            i = i + 1
        elif args[i] in "table":
            table = args[i+1]
            i = i + 1
        elif args[i] in "labels":
            i = i + 1
            while i < len(args):
                if args[i].isdigit():
                    label_stack.append(args[i])
                    i = i + 1
                else:
                    i = i - 1
                    break
        else:
            print("malformed command: ", args, " at ", args[i])
            return

        i = i + 1

    aftOpList = []
    print("gwaddr: ", gwaddr, " ifl: ", intf)
    onenh = gribi_build_one_nh(gwaddr, ifl=intf, labels=label_stack)
    print "nhadd2"
    nh = Afts.NextHopKey(index=long(nhid), next_hop=onenh)
    gribiOpList.append(AFTOperation(id=opid, network_instance=table, op=gop, next_hop=nh))
    opid = opid + 1

def process_nhgroup(args):
    global gribiRequestList, gribiOpList, opid
    print("nhgrp");

    nhid   = {}
    nhwgt  = {}
    nhbw   = {}
    nhcnt  = 0
    color  = 0

    gop = gribi_get_op(args[1])
    i = 2

    while i < len(args):
        if args[i] in [ "grpid", "nhgrpid" ]:
            nhgrpid = long(args[i+1])
            i = i + 1
        elif args[i] in [ "color", "colour" ]:
            color = long(args[i+1])
            i = i + 1
        elif args[i] in "table":
            table = args[i+1]
            i = i + 1
        elif args[i] in [ "nhop", "nexthop", "next-hop" ]:
            i = i + 1
            while i < len(args):
                if args[i] in "nhid":
                    nhid[nhcnt] = args[i+1]
                    i = i + 1
                elif args[i] in "weight":
                    nhwgt[nhcnt] = args[i+1]
                    i = i + 1
                elif args[i] in "bandwidth":
                    nhbw[nhcnt] = args[i+1]
                    i = i + 1
                else:
                    i = i - 1
                    break
                i = i + 1
            nhcnt = nhcnt + 1
        else:
            print("malformed command: ", args, " at ", args[i])
            return
        i = i + 1

    nhg = gribi_get_nhgrp(nhgrpid, color, nhcnt, nhid, nhwgt, nhbw)
    gribiOpList.append(AFTOperation(id=opid, network_instance=table, op=gop, next_hop_group=nhg))
    opid = opid + 1

def process_flush(args):
    global gribi, gribiRequestList, gribiOpList
    print("flush")

    gribiRequestList.append(ModifyRequest(operation=gribiOpList))
    gribiOpList = []

    responses = gribi.Modify(gribi_request_generator(), TIMEOUT);
    for res in responses:
        print("Received response");
        print res

def process_sleep(args):
    print("Sleeping for ", args[1])
    time.sleep(float(args[1]))

commands = {
    'connect' : setup_connection,
    'route'   : process_route,
    'nexthop' : process_nexthop,
    'nhop'    : process_nexthop,
    'nhgroup' : process_nhgroup,
    'nhgrp'   : process_nhgroup,
    'flush'   : process_flush,
    'sleep'   : process_sleep
}

def process_cmds(sargs):
    cmd = sargs[0]

    if cmd in commands:
        commands[cmd](sargs)
    else:
        print("Unknown command: ", cmd)


def Main():
    tbl     = ''
    nhcnt   = 0
    iflcnt  = 0
    lblcnt  = 0
    gwaddr  = {}
    nhlabelops = {}
    weight  = {}
    bandwidth = {}
    ifl     = {}
    pfx     = ''
    plen    = ''
    hasAttr = 0
    color   = 0
    
    noauth  = False

    global progmode
    global fmt
    global TIMEOUT
    global clientid

    timeout = 5
    bulkgetcount = 1 # no of routes per get request
    recvbuf = 0

    jsd_addr        = DEFAULT_JSD_HOST
    jsd_port        = DEFAULT_JSD_GRPC_PORT
    username        = DEFAULT_JSD_USERNAME
    password        = DEFAULT_JSD_PASSWORD
    clientid        = DEFAULT_CLIENT_ID
    cookie          = DEFAULT_APP_COOKIE
    policyname      = None

    ## set to false (default) if a direct connection to RPD
    ## set to True if a server address is passed as command line arg
    via_jsd = False

    # Parse the cmd line args
    # When no args are given, read from file /var/tmp/jrt.args


    #if len(sys.argv) != 3 or sys.argv[0] in [ "help", "--help", "-h", "usage", "--usage" ]:
    #    print (len(sys.argv))
        #print(help)
    #    print (sys.argv[2])
    #   quit()

    print (len(sys.argv))
 
    if sys.argv[1] == "-f":
        cmdfile = sys.argv[2]
        print(cmdfile)
        f = open(cmdfile, 'r')

        for line in f:
            sargv = line.split()
            print sargv
            if len(sargv):
                process_cmds(sargv)
        process_cmds(["flush"])
    quit()

if __name__ == '__main__':
    Main()