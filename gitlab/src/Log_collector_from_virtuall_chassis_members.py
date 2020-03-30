from jnpr.junos import Device
import jnpr.junos.exception as JE
import sys
from lxml import etree
import StringIO
from jnpr.junos.utils.scp import SCP
import os
from jnpr.junos.utils.start_shell import StartShell

locp = os.getcwd()
vcp = {}
hostname = '10.86.2.54'

def connect(hostname):
    try:
        dev = Device(host = hostname, user='james', passwd='juniper1')
        dev.open()
        dev.timeout = 1800
        print "Connected"
        return dev
    except JE.ConnectAuthError:
        print "Username or password is incorrect"
        sys.exit()


def upload_local(dev, all_collected_logs):
    try:
        for my_file in all_collected_logs:
            print "Trying to copy file {}".format(all_collected_logs[my_file])
            with SCP(dev, progress = True) as scp1:
                log = all_collected_logs[my_file]
                scp1.get(log, local_path=locp)
    except:
        print "Can't upload a file from the router"
        sys.exit()
    try:
        for file_to_delete in all_collected_logs:
            print "Deleting {}".format(all_collected_logs[file_to_delete])
            dev.rpc.file_delete(path = all_collected_logs[file_to_delete])
            print "Deleted"
    except:
        print "Can't delete"


def execute(dev):
    all_collected_logs = {}
    a =  dev.cli('show virtual-chassis')
    b = dev.rpc.get_software_information().xpath('//host-name')[0].text
    c = dev.rpc.get_software_information().xpath('//re-name')[0].text
    buf = StringIO.StringIO(a)
    for i in  buf.readlines():
        if 'FPC' in i:
            if 'vcp' in i:
                print "FPC {} present".format(i.split()[2].strip(')'))
                if "Master" in i:
                    vcp[i.split()[2].strip(')')] = 'Master'
                    master = i.split()[2].strip(')')
                elif "Backup" in  i:
                    vcp[i.split()[2].strip(')')] = 'Backup'
                elif "Linecard" in i:
                    vcp[i.split()[2].strip(')')] = 'Linecard'


    filename = '{}-{}.tgz'.format(b,c)
    my_path = "/var/tmp/{}".format(filename)
    filename.strip()
    print "Archiving on FPC{} - Master".format(master)
    dev.rpc.file_archive(source = '/var/log/',destination = '/var/tmp/{}'.format(filename), compress = True)
    print "Archived on FPC{} - Master".format(master)
    all_collected_logs[master] = my_path
    for every_element in vcp:
        if 'Backup' in vcp[every_element] or 'Linecard' in vcp[every_element]:
            print "Archiving on FPC{} - {}".format(every_element, vcp[every_element])
            with StartShell(dev) as ss:
                if ss.run('cli', '>'):
                    if ss.run("request session member {}".format(every_element)):
                        if ss.run('cli', '>'):
                            data = ss.run("file archive source /var/log destination fpc{}:/var/tmp/BACKUP-LOG_{}.log.tgz".format(master,every_element), "> ")
                            print "Archived on FPC{} - {}".format(every_element, vcp[every_element])
                            all_collected_logs[every_element] = '/var/tmp/BACKUP-LOG_{}.log.tgz.tar'.format(every_element)


    return filename, vcp, my_path, all_collected_logs

dev = connect(hostname)
filename, vcp, my_path, all_collected_logs = execute(dev)
upload_local(dev, all_collected_logs)