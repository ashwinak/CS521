from jnpr.junos import Device
import os,sys
import time
from lxml import etree
from jnpr.junos.utils.config import Config
from jnpr.junos.utils.scp import SCP
from  datetime import date
import jnpr.junos.exception as JE
import getpass
import lxml
from termcolor import colored
from xml.dom.minidom import parse, parseString

host = 'rppdt-mx960x.englab.juniper.net'
time_s = 20

def connect():
    try:
        dev = Device(host = host, user='regress', passwd='MaRtInI')
        dev.open()
        return dev
    except JE.ConnectAuthError:
        print "Username or password is incorrect"
        sys.exit()
def fpc_number(dev):
    fpc_list = []
    fpc_req = dev.rpc.get_fpc_information()
    for f in fpc_req.xpath('fpc'):
        if f.xpath('state')[0].text == 'Online':
            print "FPC {} is Online".format(f.xpath('slot')[0].text)
            fpc_list.append(f.xpath('slot')[0].text)
    return fpc_list

def get_pfe_data(dev, fpc_list):
    brdiscard = []
    fdiscard = []
    tkdiscard = []
    derror = []
    tdiscard = []
    bttdiscard = []
    sudiscard = []
    nhdiscard = []
    sodiscard = []
    iidiscard = []
    icdiscard = []
    ichecksum = []
    omtu = []
    ipps = []
    opps = []
    for item in fpc_list:
        pfe = etree.tostring(dev.rpc.get_pfe_statistics(fpc = item))
        dom = parseString(pfe)
        brdiscard.append(int(dom.getElementsByTagName("bad-route-discard")[0].firstChild.data))
        tkdiscard.append(int(dom.getElementsByTagName("truncated-key-discard")[0].firstChild.data))
        derror.append(int(dom.getElementsByTagName("data-error-discard")[0].firstChild.data))
        tdiscard.append(int(dom.getElementsByTagName("timeout-discard")[0].firstChild.data))
        bttdiscard.append(int(dom.getElementsByTagName("bits-to-test-discard")[0].firstChild.data))
        sudiscard.append(int(dom.getElementsByTagName("stack-underflow-discard")[0].firstChild.data))
        nhdiscard.append(int(dom.getElementsByTagName("nexthop-discard")[0].firstChild.data))
        fdiscard.append(int(dom.getElementsByTagName("fabric-discard")[0].firstChild.data))
        sodiscard.append(int(dom.getElementsByTagName("stack-overflow-discard")[0].firstChild.data))
        iidiscard.append(int(dom.getElementsByTagName("invalid-iif-discard")[0].firstChild.data))
        icdiscard.append(int(dom.getElementsByTagName("info-cell-discard")[0].firstChild.data))
        ichecksum.append(int(dom.getElementsByTagName("input-checksum")[0].firstChild.data))
        omtu.append(int(dom.getElementsByTagName("output-mtu")[0].firstChild.data))
        ipps.append(int(dom.getElementsByTagName("input-pps")[0].firstChild.data))
        opps.append(int(dom.getElementsByTagName("output-pps")[0].firstChild.data))
    return {'bad-route-discard':brdiscard, 'fabric-discard': fdiscard, 'truncated-key-discard': tkdiscard, 'data-error-discard': derror, 'timeout-discard': tdiscard, 'bits-to-test-discard':bttdiscard, 'stack-underflow-discard': sudiscard, 'nexthop-discard': nhdiscard, 'stack-overflow-discard': sodiscard, 'invalid-iif-discard': iidiscard, 'info-cell-discard': icdiscard, 'input checksum': ichecksum, 'output mtu': omtu}, {'Input packets/ps': ipps, 'Output packets/ps': opps}

def compare(fpc_list, stats, stats2):
    for p in range(len(fpc_list)):
        print '------------------------------------'
        print colored("FPC {} report: - {} seconds".format(fpc_list[p], time_s), 'green')
        print '------------------------------------'
        print colored('Input packets per second: {}'.format(traff2['Input packets/ps'][p]), 'blue')
        print colored('Output packets per second: {}'.format(traff2['Output packets/ps'][p]), 'blue')
        for d in stats:
            print colored('{} -- {} {} '.format(d, stats[d][p], stats2[d][p]), 'white'), colored('Total amount of droped packets is {} - {} packets/sec'.format(stats2[d][p] - stats[d][p], (stats2[d][p] - stats[d][p])/time_s), 'green')

dev = connect()
fpc_list = fpc_number(dev)
stats, traff = get_pfe_data(dev,fpc_list)
time.sleep(time_s)
stats2, traff2 = get_pfe_data(dev,fpc_list)
compare(fpc_list, stats, stats2)

