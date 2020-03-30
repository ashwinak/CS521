import os
import paramiko
import getpass
import re
import sys
import scp
from datetime import datetime


def printResult (release, images_dest_dict):

    """
    Function gets dictionary containing (images, md5) and prints download links and md5
    """
    print ('INTERNAL EMAIL')
    print('=' * 15 +'\n')

    print("To: Priority One Push <priority1push@juniper.net>; Compliance_helpdesk@juniper.net")
    print("Cc: google-prod-re <google-prod-re@juniper.net>; google-prod-se-team <google-prod-se-team@juniper.net>")
    print("Subject Line: Priority One Release: Google Inc")
    print("\nEmail body: \n")

    for key in images_dest_dict:
        print(format(key))

    print('\n' * 2)

    print('EXTERNAL EMAIL')
    print('=' * 15 +'\n')
    print("\nNOTE: Please copy the following teams:")
    print("Cc: JTS <juniperstaff@google.com>; google-prod-re <google-prod-re@juniper.net>; google-prod-se-team <google-prod-se-team@juniper.net>")
    print('\nDownload Links for {}'.format(release))
    print('-' * 32 +'\n')

    # Print download links:
    for key in images_dest_dict:
        print("https://download.juniper.net/software/junos/regressed/{}".format(key))

    print('\n' * 2)
    # print md5
    print('+'+'-' * 94+'+')
    print('| {:^50} | {:^40}|'.format('JUNOS Image', 'MD5'))
    print('+'+'-' * 94+'+')
    for key, value in images_dest_dict.items():
        fmt = '| {:50} | {:40}|'
        print (fmt.format(key, value))
    print('+'+'-' * 94+'+')



def getMD5sum (ssh, images_list):

    """
    Function receives a list of image_paths and returns a dict (k,v) of (image_name, md5)
    """
    #print ('Computing MD5 for files @ ')
    md5_dict = {}

    for image in images_list:
        image_name = os.path.basename(image)
        #print(image_name)
        md5_cmd = 'md5sum ' + image
        #print(md5_cmd)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(md5_cmd)
        md5sum = ssh_stdout.read(33).decode('utf-8')
        md5_dict[image_name] = md5sum

    return md5_dict


def scpFiles(ssh, images_list):

    """
    Function to scp files from  volume/build/junos/MAIN_BRANCH/service/JUNOS_VERSION/*
    to /volume/download/docroot/software/Predeploy/'
    """

    dst = '/volume/download/docroot/software/Predeploy/'
    print ("Copying required files to /volume/download/docroot/software/Predeploy/\n\n")
    print ("please wait ....\n\n")
    for image in images_list:
         #print (image)
         #src = '/volume/build/junos/17.2/service/17.2X75-D91.5/mksb.log'
         cmd = 'scp '+image+' '+dst
         print(cmd)
         ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
         print('-->'+ssh_stdout.read().decode('utf-8'))



def getInput():

    """
    Function to get release, username and password
    """
    while True:  # repeat forever
        release = input('Enter full JUNOS release name:')

        while not re.match (r'(\d+.\d\w\d+\-\w\d+.\d)|(\d+.\d\w\d+\-\w\d+)', release):
            release = input('Incorrect cloud release name. Enter full JUNOS release name:')

        release_again = input('Confirm JUNOS release name:')
        if release != release_again:
         print ("Release names don't match .Please try again!!")
        else:
            break

    username = input('Username:')
    password = getpass.getpass(prompt='UNIX password:')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect('contrail-ubm-dilipct01.svec1.juniper.net', username=username, password=password, timeout=10)
        return (release, username, password, ssh)
    except paramiko.AuthenticationException as authenticationException:
        print("Authentication failed, please verify your credentials: %s" % authenticationException)
        sys.exit(0)
    except paramiko.SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
        sys.exit(0)
    except paramiko.BadHostKeyException as badHostKeyException:
        print("Unable to verify server's host key: %s" % badHostKeyException)
        sys.exit(0)


def main():

    """
    Main function to execute other functions
    """
    timestamp = datetime.now().strftime('%c')
    print(timestamp)

    #release = '17.2X75-D90.4'

    release, username, password, ssh = getInput()

    images_src = """
            /volume/build/junos/MAIN_BRANCH/service/JUNOS_VERSION/ship/jinstall-JUNOS_VERSION-signed.tgz
            /volume/build/junos/MAIN_BRANCH/service/JUNOS_VERSION/ship/jinstall64-JUNOS_VERSION-signed.tgz
            /volume/build/junos/MAIN_BRANCH/service/JUNOS_VERSION/ship/jinstall-ppc-JUNOS_VERSION-signed.tgz
            /volume/build/junos/MAIN_BRANCH/service/JUNOS_VERSION/ship/junos-install-mx-x86-64-JUNOS_VERSION.tgz
            /volume/build/junos/MAIN_BRANCH/service/JUNOS_VERSION/ship/junos-install-ptx-x86-64-JUNOS_VERSION.tgz
            /volume/build/junos/MAIN_BRANCH/service/JUNOS_VERSION/ship/junos-vmhost-install-ptx-x86-64-JUNOS_VERSION.tgz
            /volume/build/junos/MAIN_BRANCH/service/JUNOS_VERSION/telemetry/ship/network-agent-x86-32-JUNOS_VERSION-C1.tgz 
            """.replace('JUNOS_VERSION', release).replace('MAIN_BRANCH', release[:4])

    images_src_list = images_src.split()
    #print (images_src_list)

    images_dest = """
            /volume/download/docroot/software/Predeploy/jinstall-JUNOS_VERSION-signed.tgz
            /volume/download/docroot/software/Predeploy/jinstall64-JUNOS_VERSION-signed.tgz
            /volume/download/docroot/software/Predeploy/jinstall-ppc-JUNOS_VERSION-signed.tgz
            /volume/download/docroot/software/Predeploy/junos-install-mx-x86-64-JUNOS_VERSION.tgz
            /volume/download/docroot/software/Predeploy/junos-install-ptx-x86-64-JUNOS_VERSION.tgz
            /volume/download/docroot/software/Predeploy/junos-vmhost-install-ptx-x86-64-JUNOS_VERSION.tgz
            /volume/download/docroot/software/Predeploy/network-agent-x86-32-JUNOS_VERSION-C1.tgz
            """.replace('JUNOS_VERSION', release)

    images_dest_list = images_dest.split()
    #print (images_dest_list)


    #ssh.connect('svl-jtac-lnx01.juniper.net', username='rvenkat', password='******', timeout=40)

    scpFiles(ssh, images_src_list)
    md5dict_src = getMD5sum(ssh, images_src_list)
    md5dict_dest = getMD5sum(ssh, images_dest_list)

    if md5dict_src == md5dict_dest:
        printResult(release, md5dict_dest)
        print('\nSuccess !!! All files copied to /volume/download/docroot/software/Predeploy/\n')
    else:
        print("""\nDrat !! Something went wrong.\n
        1. Check manually if all files are present in /volume/download/docroot/software/Predeploy/'\n
        2. if all files are present check if md5sum at source and /volume/download/docroot/software/Predeploy/ is correct\n""")

    print ('*** END ***')

    ssh.close()


if __name__ == '__main__':
    main()


