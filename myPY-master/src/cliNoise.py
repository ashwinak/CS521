#!/usr/bin/env python
import atexit
import paramiko
import time
import sys

if len(sys.argv) == 1:
    print "This script uses file called cmd.txt that contains all commands to be collected, one command per line."
    sys.exit()


class MySSH:

    def __init__(self, host, user, password, port = 22):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=port, username=user, password=password)
        atexit.register(client.close)
        self.client = client

    def __call__(self, command):
        stdin,stdout,stderr = self.client.exec_command(command)
        sshdata = stdout.readlines()
        for line in sshdata:
            print(line)


try:
    while True:
        with open('cmd.txt') as f:
            cmd = f.readlines()
            remote = MySSH('192.168.0.12', 'regress', 'MaRtInI')
            for i in range(len(cmd)):
                print cmd[i]
                remote(cmd[i])
                time.sleep(2)
except KeyboardInterrupt:
    print "User interrupted"
