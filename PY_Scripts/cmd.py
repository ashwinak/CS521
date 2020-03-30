import paramiko
try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('15.168.0.3', username='lab', password='lab123')
    while True:
        with open('cmd.txt') as f:
            cmd = f.readlines()
            stdin, stdout, stderr = client.exec_command('cmd[1]')
            for line in stdout:
                print line.strip('\n')
            client.close()
except KeyboardInterrupt:
    print "User interrupted"

