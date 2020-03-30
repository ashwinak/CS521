import os, sys, logging
from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import *
from  datetime import date
import time
from lxml import etree
import random
from jnpr.junos.utils.config import Config
from netaddr import IPAddress
from netaddr import IPNetwork
from jinja2 import Template

host = 'nationx.englab.juniper.net'
locp = os.getcwd()
subnets = []
subnets6 = []

def connect():
    dev = Device(host = host, user='regress', passwd='MaRtInI')
    dev.open()
    print 'Connected'

    return dev

def networks():
    for ip in IPNetwork('100.100/18'):
        subnets.append(str(ip))
    for ip6 in IPNetwork('2121::2121/117'):
        subnets6.append(str(ip6))
    return subnets,subnets6

def jinja_load(dict, dict6):
    template = open('{}/static.conf'.format(locp), 'r').read()
    template_jinja = Template(template)
    config = template_jinja.render(dict)
    file = open('{}/new_file.conf'.format(locp), 'w')
    file.write(config)
    template6 = open('{}/static6.conf'.format(locp), 'r').read()
    template_jinja6 = Template(template6)
    config6 = template_jinja6.render(dict6)
    file6 = open('{}/new_file6.conf'.format(locp), 'w')
    file6.write(config6)
    file6.close()
    print "Both configs are generated"
    return config, config6

def load_juniper(dev):
    dev.bind(cu=Config)
    dev.cu.lock()
    dev.cu.load(path='{}/new_file.conf'.format(locp), merge=True)
    dev.cu.load(path='{}/new_file6.conf'.format(locp), merge=True)
    dev.cu.commit()
    print "Configs are loaded to the router"
dev=connect()
subnets, subnets6 = networks()
dict = {'item':subnets}
dict6 = {'item':subnets6}
jinja_load(dict, dict6)
load_juniper(dev)

