import os, sys, logging
from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import *
from  datetime import date
import time
from lxml import etree
import random
from jnpr.junos.utils.config import Config

host = '10.111.111.1'
list1 = []

def connect():
    dev = Device(host = host, user='regress', passwd='MaRtInI')
    dev.open()
    return dev

dev = connect()
dev.bind(cu=Config)
dev.cu.lock()

for y in range(720):
    for i in range(16):
        list1.append(random.randint(1000,1600))

    for x in list1:
        command = 'set interfaces gr-1/0/0.{} disable'.format(x)
        print 'interface gr-1/0/0.{} has been disabled'.format(x)
        dev.cu.load(command, format='set')


    dev.cu.commit()
    time.sleep(15)
    for x in list1:
        command = 'delete interfaces gr-1/0/0.{} disable'.format(x)
        print 'interface gr-1/0/0.{} has been enabled'.format(x)
        try:
            dev.cu.load(command, format='set')
        except KeyboardInterrupt:
            sys.exit()
        except:
            print 'Interface gr-1/0/0.{} is already enabled'
    dev.cu.commit()
    time.sleep(15)
    list1 = []
dev.close()


