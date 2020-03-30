#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import *
import sys

if len(sys.argv) != 3:
    print "%%% Usage: ./jupgrade.py <IP> <img_path>"
    sys.exit()
try:
    dev=Device(host=sys.argv[1], user='regress',passwd='MaRtInI')
    dev.open()

    def update_progress(dev,report):
        print dev.hostname, '>' , report

    sw=SW(dev)
    ok=sw.install(package=r'sys.argv[2]', progress=update_progress)
    if ok:
        print 'rebooting'
        sw.reboot()
    dev.close()
except ConnectRefusedError:
    print "%%%% Connection refused,check IP addr..."



