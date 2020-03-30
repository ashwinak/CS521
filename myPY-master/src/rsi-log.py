from jnpr.junos import Device
import os,sys
from lxml import etree
from jnpr.junos.utils.config import Config
from jnpr.junos.utils.scp import SCP
from  datetime import date
import pysftp
import jnpr.junos.exception as JE
import getpass

usr = raw_input('Username:')
pss = getpass.getpass('Password:')
host = raw_input('rootHostname:')
casenumber = raw_input('Case number:')

locp = os.getcwd()
print 'Files will be stored in ',locp

# Getting connected to the Device
def connect():
    try:
        dev = Device(host = host, user=usr, passwd=pss)
        dev.open()
        return dev
    except JE.ConnectAuthError:
        print "Username or password is incorrect"
        sys.exit()

# Getting the RSI output saved into a file on the server where the script is running
# Archiving the /var/log/* into a tgz file in the Juniper router
def collect(dev):
    path = 'rsi.{}.{}.log'.format(host, date.today())
    file = open('{}/{}'.format(locp,path), 'w')
    a = etree.tostring(dev.rpc.get_support_information())
    file.write(a)
    dev.rpc.file_archive(source = '/var/log/*', destination = 'logs.{}.{}'.format(host, date.today()), compress = True )
    return path


# Upload a /var/log/* archived tgz file into a server where the script is running
def upload_local(dev):
    try:
        with SCP(dev, progress = True) as scp1:
            log = 'logs.{}.{}.tgz'.format(host,date.today())
            scp1.get(log, local_path=locp)
            return log
    except:
        print "Can't upload a file from the router"
        sys.exit()

# Creating a /pub/incoming/casenumber dir, cd into dir and upload both files
# Using cnops to avoid a problem with the unknown ssh.hostkey
def upload_juniper(case):
    dir = '/pub/incoming/{}'.format(case)
    cnops = pysftp.CnOpts()
    cnops.hostkeys = None
    with pysftp.Connection('sftp.juniper.net', username = 'anonymous', password = 'anonymous', cnopts=cnops) as sftp1:
        try:
            sftp1.mkdir(dir)

        except IOError:
            print "Directory is already existing, starting an upload"

        with sftp1.cd('./{}/'.format(dir)):
            try:
                print 'Uploading {}/{}'.format(locp,rsi)
                sftp1.put('{}/{}'.format(locp,rsi))
                print "First file is uploaded"
            except:
                print "Can't upload {}".format(rsi)

            try:
                print 'Uploading {}/{}'.format(locp,log)
                sftp1.put('{}/{}'.format(locp,log))
                print "Second file is uploaded"
            except:
                print "Can't upload {}".format(log)

dev = connect()
rsi = collect(dev)
log = upload_local(dev)
upload_juniper(casenumber)

print "Uploaded RSI  {}".format(rsi)
print "Uploaded var/log/*  {}".format(log)

dev.close()

