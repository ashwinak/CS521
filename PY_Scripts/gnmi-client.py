#ashwinak@sv-svr1dl380-csim:~/grpc/gnmi$ more subscribe_gnmi_client_1022_sec.py

import json
import grpc
import re
import sys
import os
import logging
import math
import datetime
#from flatten_xml import gen_request

from grpc.beta import implementations
from grpc.framework.interfaces.face.face import *
#from openconfig_service_pb2 import *

from authentication_service_pb2 import *
import authentication_service_pb2
import gnmi_pb2
import argparse, time
parser = argparse.ArgumentParser()
import inspect
import gen_func
import any_pb2
import agent_pb2
from google.protobuf import json_format
# import xmltodict
import dicttoxml
import jnprheader_pb2

sensor_timestamp = []
sensor_path = []
# _TIME_OUT_SECONDS = 100000

def Main():
    try:
        flag = 0
#        config_file = "b.json"
        i = 0

        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--conf', help = 'Input Config file JSON', required = True)
        parser.add_argument('-d', '--device', help = 'Target host name', required = True)
        parser.add_argument('-l', '--logfile', help = 'Streamed data Log file', required = True)
        parser.add_argument('-i', '--intervals', default=10, help = 'Expected no. of period updates for all sensors(sum of updates for all sensors)')
        parser.add_argument('-t', '--timeout', default=100000, help = 'Subsribe() RPC timeout')
        parser.add_argument('-s', '--secure', help = 'PEM file for secure channel')
        parser.add_argument('-sk', '--securekey', help = 'Secure Key File')
        parser.add_argument('-sc', '--securecrt', help = 'Secure CRT File')
        global args
        args = parser.parse_args()

        GRPC_SERVER = json.loads(open('./%s' % args.conf).read())
        # print GRPC_SERVER
        prog = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        prog = (args.logfile)

        for logdat in GRPC_SERVER["dut_list"]:
            if logdat["verbose"]==None:
                logformat = '%(asctime)s,%(msecs)-3d %(message)s'
            else:
                logformat = '%(asctime)s,%(msecs)-3d %(levelname)-8s %(threadName)s %(message)s'

            if logdat["verbose"]==None or logdat["verbose"]==1:
                loglevel = logging.INFO
            else:
                loglevel = logging.DEBUG

            loglevel = logging.INFO
            # For supported GRPC trace options check:
            #   https://github.com/grpc/grpc/blob/master/doc/environment_variables.md

            if logdat["verbose"]==3:
              os.environ["GRPC_TRACE"] = "all"
              os.environ["GRPC_VERBOSITY"] = "ERROR"

            if logdat["verbose"]==4:
              os.environ["GRPC_TRACE"] = "api,call_error,channel,connectivity_state,op_failure"
              os.environ["GRPC_VERBOSITY"] = "INFO"

            if logdat["verbose"]==5:
              os.environ["GRPC_TRACE"] = "all"
              os.environ["GRPC_VERBOSITY"] = "INFO"

            if logdat["verbose"]==6:
              os.environ["GRPC_TRACE"] = "all"
              os.environ["GRPC_VERBOSITY"] = "DEBUG"

            timeformat = '%y/%m/%d %H:%M:%S'

            loghandler = logging.StreamHandler(logdat["log_head"])
            loghandler.setFormatter(logging.Formatter(logformat, timeformat))
            # formatter = logging.Formatter('%(asctime)s - - %(message)s')
            # loghandler.setFormatter(formatter)
            loghandler.setLevel(logging.DEBUG)

        global log

        log = logging.getLogger(prog)
        log.setLevel(logging.DEBUG)
        fh = logging.FileHandler(prog)
        fh.setFormatter(logging.Formatter(logformat, timeformat))
        log.addHandler(fh)
        # log.addHandler(loghandler)

        # console = logging.StreamHandler()
        # console.setLevel(logging.INFO)
        # console.setFormatter(formatter)
        # logger.addHandler(console)

        for dut_list in GRPC_SERVER["dut_list"]:
            if args.secure:
                print "first"
                creds = implementations.ssl_channel_credentials(open('/opt/jvision/grpc/oc/babukt/router.pem').read(), open('/opt/jvision/grpc/oc/babukt/client.key').read(), open('/opt/jvision/grpc/oc/babukt/client.crt').read())
                print "second"
                print creds
                channel = implementations.secure_channel(args.device, 50051,creds)
                stub1 = authentication_service_pb2.beta_create_Login_stub(channel)
                # channel = implementations.secure_channel(args.device, 50051, creds)
                # stub1 = authentication_service_pb2.beta_create_Login_stub(channel)
                print "fourth"
                # login_response = stub1.LoginCheck(authentication_service_pb2.LoginRequest(user_name="root",password="Embe1mpls", client_id="BC_21"),1115000)
                login_response = stub1.LoginCheck(authentication_service_pb2.LoginRequest(user_name="root",password="Embe1mpls",client_id="BC_21"),15000)
                print "fifth"

                if login_response.result == True:
                    print "ERROR: gRPC Server Connection failed!!!",+login_response.result
                    sys.exit()
                else:
                    print "gRPC Server Connection established succesfully!!!"
            else:
                channel = implementations.insecure_channel(args.device, dut_list["port"])

            global gnmi_stub_channel
            gnmi_stub_channel = gnmi_pb2.beta_create_gNMI_stub(channel)

            # print "Connected to JSD and created handle to GNMI services"

            for rpc1 in dut_list["rpc"]:
               # print rpc1
               if rpc1 ==  "sub_request":
                 # Sendsub(dut_list[rpc1])
                 SubscribeRequestMsg(dut_list[rpc1])

    except Exception as tx:
        print '%s' % (tx.message)
    return


def json_parser(opt):
    my_subs = []
    i=0
    j=0

    # if "prefix" in opt:
    #     path_elements = gen_path([opt["prefix"]])
    #     # path_elements = list_from_path(data["path"])
    #     my_prefix = gnmi_pb2.Path(elem=path_elements)
    # else:
    #     my_prefix = None

    for data in opt["subscription"]:
        if data["path"]:
            sensor_path.append(data["path"])
            # print sensor_path[j]
            j+=1
        else:
            my_path = None

        if data["submode"]:
            sub_mode = data["submode"]
        else:
            sub_mode = None

        if "sample_interval" in data:
            my_sample_interval = data["sample_interval"]
            sensor_timestamp.append(data["sample_interval"])
            # print "value of interval"
            # print sensor_timestamp[i]
            i+=1
        else:
            sensor_timestamp.append(30000000000)
            my_sample_interval = None



    if "use_aliases" in opt:
        my_aliases = opt["use_aliases"]
    else:
        my_aliases = None

    if "qos" in opt:
        my_qos = gnmi_pb2.QOSMarking(marking=opt["qos"])
    else:
        myqos = None

    if "mode" in opt:
        my_mode = opt["mode"]
    else:
        my_mode = None

    if "allow_aggregation" in opt:
        my_allow_aggregation = opt["allow_aggregation"]
    else:
        my_allow_aggregation = None

    if "poll" in opt:
        my_poll = gnmi_pb2.Poll()
    else:
        my_poll = None


def SubscribeRequestMsg(opt):
    mysubs = []
    # print opt
    req_iterator = gen_func.gen_subscribe(opt)

    json_parser(opt)
    msgs = 0
    upds = 0
    secs = 0
    start = 0
    time1 = 0
    time2 = 0
    sensor_len= len(sensor_path)
    timestamp_len= len(sensor_timestamp)
    time_stamp = [[],[],[],[],[],[],[]]
    path_sensor = []
    a=0
    b = [0,0,0,0,0,0,0,0,0,0]
    my_iter = 0
    exit_response = 0
    first_prefix = 0;
    oc_log = {}
    try:
        responses = gnmi_stub_channel.Subscribe(req_iterator, int(args.timeout))
        ts = time.time()
        size = 0
        # oc_log['subscribe_sent'] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        # oc_log['subscribe_sent'] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        for response in responses:
            # oc_log['subscribe_ack'] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            if exit_response:
                break
            if response.HasField('sync_response'):
                log.debug('Sync Response received\n'+str(response))
                # secs += time.time() - start
                # start = 0
            elif response.HasField('update'):
                if start==0:
                    start=time.time()
                # if first_prefix == 0:
                #     first_prefix = response.update.prefix

                # first_prefix = response.update.prefix
                msgs += 1
                upds += len(response.update.update)
                time.time() - start
                secs += time.time() - (start+secs)
                # ts = time.time()
                log.info('Update received\n'+str(response))
                log.info("%d updates and %d messages within %1.2f seconds", upds, msgs, secs)
                # oc_log['subscribe_sent'] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# condition for verifying sensors and timestamp
                # response_lll = str(response)
                # for index, sensor in enumerate(sensor_path):
                #     if re.search(sensor, response_lll):
                #         for result in response.update.update:
                #             if "__junos_re_stream_creation_timestamp__" in str(result.path):
                #                 a=result.val.uint_val
                #                 # print "a vaue:", a
                #                 # print "b bfore vaue:", b
                #                 if b[index] != a:
                #                     my_iter += 1
                #                     if my_iter > int(args.intervals) :
                #                         exit_response = 1
                #                     b[index]=a
                #                     # print "Apending b value:", b
                #                     time_stamp[index].append(b[index])
                #                             #        # print time_stamp
                #             elif "__juniper_telemetry_header__" in str(result.path):
                #                 x = jnprheader_pb2.GnmiJuniperTelemetryHeader()
                #                 result.val.any_val.Unpack(x)
                #                 log.info('Header received\n'+str(x))

                len_timestamp=len(time_stamp)
                size += response.ByteSize()
                siz = response.ByteSize()
                log.info("size is :"+str(size)+"\n\n")
                # log.info("Current size is :"+str(size)+"\n\n")
                # print siz

            else:
                log.error('Unknown response received:\n'+str(response))

        print "Received timestamp for sensors:\n", time_stamp
        # for index, sensor in enumerate(sensor_path):
        #
        #     print "-------------------------------------------------------------------------------------"
        #     print "   Checking correctness of sample intervals in streamed data for sensor", sensor
        #     print "-------------------------------------------------------------------------------------"
        #
        #     len_timestamp=len(time_stamp[index])
        #     print "length %d" % len_timestamp
        #     if len_timestamp:
        #
        #         diff = [x - time_stamp[index][i - 1] for i, x in enumerate(time_stamp[index])][1:]
        #         print "Consequitive sample interval difference", diff, "\n"
        #         final_timestamp=math.ceil(sensor_timestamp[index]/1000000000)
        #
        #         for i in range(0,len(diff)):
        #
        #             # print "with out ceil %d" % (diff[i]/1000)
        #
        #             temp_timestamp = math.ceil(int(diff[i]/1000))
        #             # print "ceil value"
        #             # print temp_timestamp
        #             # if temp_timestamp != final_timestamp:
        #             #     print "TESTCASE FAILED: update", i, "not received within sample interval for sensor", sensor
        #             # else:
        #             #     print "TESTCASE PASSED: update", i, "received within sample interval for sensor", sensor
        #             #
        #             if (temp_timestamp == final_timestamp or \
        #                 temp_timestamp == final_timestamp+1 or \
        #                 temp_timestamp == final_timestamp-1 ) :
        #                 print "TESTCASE PASSED: update", i, "received within sample interval for sensor", sensor
        #             else:
        #                 print "TESTCASE FAILED: update", i, "not received within sample interval for sensor", sensor



    except grpc.RpcError as x:
        # log.error("grpc.RpcError received:\n%s", x.details)
        print "grpc.RpcError received:", x.code, x.details
    except AbortionError as inst:
        # log.error("AbortionError received:\n%s", inst.details)
        print "AbortionError received:", inst.code, inst.details
    except ExpirationError as X:
        print "ExpirationError received:", X.code, X.details
    except Exception as inst:
        print inst
    except KeyboardInterrupt as user:
        print ("Stopped by user", user)


if __name__ == '__main__':
   Main()