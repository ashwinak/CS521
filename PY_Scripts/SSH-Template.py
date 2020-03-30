#!/usr/bin/python
import paramiko
import time
import re
import sys

#Open SSHv2 connection to devices

def open_ssh_conn(ip):
    #Change exception message
    try:
        #Define SSH parameters
        selected_user_file = open('credentials.txt', 'r')
        
        #Starting from the beginning of the file
        selected_user_file.seek(0)

        username = selected_user_file.readlines()[0].split(',')[0]
        
        #Starting from the beginning of the file
        selected_user_file.seek(0)
        
        password = selected_user_file.readlines()[0].split(',')[1]
        
        #Logging into device
        session = paramiko.SSHClient()

        session.set_missing_host_key_policy(
                paramiko.AutoAddPolicy())
                
        session.connect(ip, username = username, password = "MaRtInI")
        
        connection = session.invoke_shell()	
        
        #Setting terminal length for entire output - no pagination
        connection.send("cli\n")
        time.sleep(1)
        
        #Entering global config mode
        #connection.send("\n")
        #connection.send("\n")
        #time.sleep(1)
        
        #Open user selected file for reading
        selected_cmd_file = open('commands.txt', 'r')
            
        #Starting from the beginning of the file
        selected_cmd_file.seek(0)
        
        #Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)
        
        #Closing the user file
        selected_user_file.close()
        
        #Closing the command file
        selected_cmd_file.close()
        
        #Checking command output for IOS syntax errors
        output = connection.recv(65535)
        print output
        
        if re.search(r"error", output):
            print "* There was at least one JUNOS syntax error on device %s" % ip
        else:
            print "\nDONE for device %s" % ip
            
        #Test for reading command output
        #print output + "\n"
        
        #Closing the connection
        session.close()
     
    except paramiko.AuthenticationException:
        print "* Invalid username or password. \n* Please check the username/password file or the device configuration!"
        print "* Closing program...\n"
		
# Calling the SSH function

open_ssh_conn("172.19.64.63")
