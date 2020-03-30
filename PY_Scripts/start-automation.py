import os
import time
import sys
import random
import string

try:
    if len(sys.argv) == 1:
        print "####Usage: python start-automation.py  <IP>"
        sys.exit()
    print "Creating config JSON files..."
    alnum = string.ascii_letters + string.digits
    an = ""
    for i in range(5):
        an = an + random.choice(alnum)
        #print an
    s = open("172-master.json").read()
    s = s.replace('DUT', sys.argv[1])
    s = s.replace('ID', sys.argv[1] + an)
    f = open(sys.argv[1] + '.json', 'w')
    f.write(s)
    f.close()
    print "Creating WAN delays of 100ms..."
    os.system("echo \'lab1234\' | sudo -S tc qdisc del dev ens3f0 root")
    os.system("echo \'lab1234\' | sudo -S tc qdisc add dev ens3f0 root netem delay 100ms")
    os.system("echo \'lab1234\' | sudo -S tc -s qdisc ls dev ens3f0")
    print "Killing old sessions..."
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep .json | grep sudo | awk {'print $2'})")
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep .json | grep sudo | awk {'print $2'}i)")
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep ./jtimon | awk {'print $2'})")
    print "Starting new sessions..."
    os.system('rm -rf ' + sys.argv[1] + '.log')
    os.system('echo \'lab1234\' | sudo -S nohup ./jtimon-ssl --config '+ sys.argv[1] + '.json --drop-check --log '+ sys.argv[1] +'.log &')
except KeyboardInterrupt:
    print "User interrupted"