#!/usr/bin/env python3

import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException

def enable_netconf(net_device):
    print ('{} Connecting to {}'.format(time.asctime(), net_device["ip"]))
    junos_device = ConnectHandler(**net_device)
    configure = junos_device.config_mode()
    print ('{} Applying configuration to {}'.format(time.asctime(), net_device["ip"]))
    setssns = junos_device.send_command('set system services netconf ssh')
    print ('{} Committing configuration to {}'.format(time.asctime(), net_device["ip"]))
    junos_device.commit(comment='Enabled NETCONF service', and_quit=True)
    print ('{} Closing connection to {}'.format(time.asctime(), net_device["ip"]))
    junos_device.disconnect()

def main():
    user_login = input("Username: ")
    user_pass = getpass("Password: ")
    with open("inventory.txt") as f:
        device_list = f.read().splitlines()
        for device in device_list:
            net_device = {
                'device_type': 'juniper',
                'ip': device,
                'username': user_login,
                'password': user_pass,
            }
            enable_netconf(net_device)

if __name__ == '__main__':
    main()