#! /usr/bin/env python
import sys
import os
import subprocess
if len(sys.argv) < 3:
    print ("Usage python psswdless.py <remote ip> <uname>")
    sys.exit()
else:
    key=os.system("ls -lrt ~/.ssh/id_rsa.pub")
    if key == 0:
        print ("###Public key already exist")
    else:
        os.system('ssh-keygen -b 2048 -t rsa -f $HOME/.ssh/id_rsa -q -N ""')

print ("Remote host is %s...." %sys.argv[1])
print ("Finding home directory in remote host...")
#home_dir = str(os.system('ssh -o StrictHostKeyChecking=no ' + sys.argv[2] + '@' + sys.argv[1] + " \'echo $HOME\'"))
home_dir = subprocess.check_output('ssh -o StrictHostKeyChecking=no ' + sys.argv[2] + '@' + sys.argv[1] + " \'echo $HOME\'", shell=True).decode('ascii').strip()
print ("Remote home directory is ",home_dir)
print ("Creating remote ssh directory...")
print('ssh -o StrictHostKeyChecking=no ' + sys.argv[2] + '@' + sys.argv[1] + ' mkdir -p ' +home_dir+ '/.ssh')
os.system('ssh -o StrictHostKeyChecking=no ' + sys.argv[2] + '@' + sys.argv[1] + ' mkdir -p ' +home_dir+ '/.ssh')
print ("Copying local pub key to remote home_dir/.ssh/authorized_keys")
#print("cat ~/.ssh/id_rsa.pub |ssh "  + sys.argv[2] + '@' + sys.argv[1] + " cat >> " + home_dir + "/.ssh/authorized_keys")
os.system("cat ~/.ssh/id_rsa.pub |ssh "  + sys.argv[2] + '@' + sys.argv[1] + " \'cat >> " + home_dir + "/.ssh/authorized_keys\'")
print ("Changing permissions for remote ~/.ssh/authorized_keys")
#print('ssh ' + sys.argv[2] +'@' + sys.argv[1] + " chmod 700 .ssh; chmod 640 " +home_dir+ "/.ssh/authorized_keys")
os.system('ssh ' + sys.argv[2] +'@' + sys.argv[1] + " \'chmod 700 .ssh; chmod 640 " +home_dir+ "/.ssh/authorized_keys\'")

'''
Execution logs:

(base) ashwinak-mbp:PY_Scripts ashwinak$ ./psswdless.py 10.13.120.104 csim
-rw-r--r--  1 ashwinak  staff  403 Jan 25  2019 /Users/ashwinak/.ssh/id_rsa.pub
###Public key already exist
Remote host is 10.13.120.104....
Finding home directory in remote host...
Warning: Permanently added '10.13.120.104' (ECDSA) to the list of known hosts.
csim@10.13.120.104's password:
Remote home directory is  /home/csim
Creating remote ssh directory...
ssh -o StrictHostKeyChecking=no csim@10.13.120.104 mkdir -p /home/csim/.ssh
csim@10.13.120.104's password:
Copying local pub key to remote home_dir/.ssh/authorized_keys
csim@10.13.120.104's password:
Changing permissions for remote ~/.ssh/authorized_keys
(base) ashwinak-mbp:PY_Scripts ashwinak$ ssh csim@10.13.120.104
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-116-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

246 packages can be updated.
141 updates are security updates.


Last login: Mon Sep 23 07:52:21 2019 from 172.29.103.14
csim@Server-B:~$
'''
