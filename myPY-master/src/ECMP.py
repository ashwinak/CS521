from jnpr.junos import Device
import jnpr.junos.exception as JE
import sys
import argparse
from lxml import etree


parser = argparse.ArgumentParser('Shows a deviation on Output bps for al LAG members')
parser.add_argument("-i", help = "AE interface", required = True)
parser.add_argument("-r", help = "Router name/IP", required = True)

args = parser.parse_args()

hostname =  args.r
interface = args.i
summary = {}
num = 0

def check(intertface):
    if 'ae' not in interface:
        print "An interface has to be AE"
        sys.exit()


def connect(hostname):
    try:
        dev = Device(host = hostname, user='csim', passwd='Juniper123')
        dev.open()
        dev.timeout = 1800
        return dev
    except JE.ConnectAuthError:
        print "Username or password is incorrect"
        sys.exit()

def execute(dev):
    maximum = 0
    total = 0
    total_int_number = 0
    my_rpc = dev.rpc.get_interface_information(level = 'extensive', interface_name = interface)
    for member in my_rpc.xpath('//lag-link'):
        total_int_number = total_int_number + 1
        lag = member.xpath('./name')[0].text.strip()
        bw = member.xpath('./output-bps')[0].text.strip()
        summary[lag] = bw
        total = total + int(bw)
    expected = float(total / total_int_number)
    for d in summary:
        absolute = float(abs((int(summary[d]) - expected)))
        print "{} - Output Bps is {}, Deviation in Bps is {} , which is {} percent".format(d, summary[d], absolute, (absolute/expected)*100)
        if (absolute/expected)*100 > maximum:
            maximum = (absolute/expected)*100
            max_int = d
    print "The biggest deviation from the average is on {} - {}%".format(max_int, maximum)



check(interface)
dev = connect(hostname)
execute(dev)










