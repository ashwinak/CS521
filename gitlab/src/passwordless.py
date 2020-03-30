#! /usr/bin/env python
import sys
import os
if len(sys.argv) < 2:
    print "Usage python psswdless.py <remote ip>"
    sys.exit()
else:
    key=os.system("ls -lrt ~/.ssh/id_rsa.pub")
    if key == 0:
        print "###Public key already exist"
    else:
        os.system('ssh-keygen -b 2048 -t rsa -f /Users/ashwinak/.ssh/id_rsa -q -N ""')

print "###Creating .ssh dir in remote host...."
#rhost=sys.argv[1]
print "Remote host is %s...." %sys.argv[1]
print "Creating remote ssh directory..."
os.system('ssh -o "StrictHostKeyChecking no" ashwinak@' + sys.argv[1] + ' mkdir -p .ssh')
print "Copying local pub key to remote ~/.ssh/authorized_keys"
os.system("cat ~/.ssh/id_rsa.pub |ssh ashwinak@" + sys.argv[1] + " 'cat >> ~/.ssh/authorized_keys'")
print "Changing permissions for remote ~/.ssh/authorized_keys"
os.system('ssh ashwinak@' + sys.argv[1] + " chmod 700 .ssh; chmod 640 ~/.ssh/authorized_keys")