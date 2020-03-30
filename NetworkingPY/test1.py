import os
import sys

try:
    print "Killing old sessions..."
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep .json | grep sudo | awk {'print $2'})")
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep .json | grep sudo | awk {'print $2'}i)")
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep ./jtimon | awk {'print $2'})")
    os.system("echo \'lab1234\' | sudo -S kill -9 $(ps -aux | grep ./jtimon | awk {'print $2'})")
    os.system("ps -aux | grep ./jtimon | grep -v grep")
except KeyboardInterrupt:
    print "User interrupted"