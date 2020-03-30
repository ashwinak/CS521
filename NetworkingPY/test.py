import os
import time
import sys
from random import randint

try:
    if len(sys.argv) == 1:
        print "####Usage jti <IP>"
        sys.exit()
    print "Creating config JSON files..."
    with open("172-masterpy.json", "rt") as fin:
        with open(sys.argv[1] + '.json', "wt+") as fout:
            for line in fin:
                fout.write(line.replace('DUT', sys.argv[1]))
            fout.close
    fin.close
    print "Creating WAN delays of 100ms..."
    os.system("echo \'lab1234\' | sudo -S tc qdisc del dev ens1f0 root")
    os.system("echo \'lab1234\' | sudo -S tc qdisc add dev ens1f0 root netem delay 100ms")
    os.system("echo \'lab1234\' | sudo -S tc -s qdisc ls dev ens1f0")
    print "Killing old sessions..."
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep .json | grep sudo | awk {'print $2'})")
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep .json | grep sudo | awk {'print $2'}i)")
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep ./jtimon | awk {'print $2'})")
    print "Starting new sessions..."
    os.system("echo \'lab1234\' | sudo -S nohup ./jtimon -ssl --config sys.argv[1].json --drop-check --log sys.argv[1].log &")
except KeyboardInterrupt:
    print "User interrupted"