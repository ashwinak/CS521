#!/usr/bin/python
import os
PCAP = raw_input('Enter PCAP name: ')
SMAC = raw_input('Enter source MAC: ')
DMAC = raw_input('Enter dst MAC: ')
SIP = raw_input('Enter Src IP: ')
DIP = raw_input('Enter Dst IP: ')
cmd = "tcpprep --auto=bridge --pcap=" + PCAP[0:] + " --cachefile=" + PCAP[0:] + ".cache"
os.system(cmd)
cmd1 = "tcprewrite --endpoints=" + DIP[0:] + ":" + SIP[0:] + " --cachefile=" + PCAP[0:] + ".cache" + " --infile=" +PCAP[0:] + " 
--outfile=" + PCAP[0:] + "1"
os.system(cmd1)
cmd2= "tcprewrite  --enet-dmac=" +DMAC[0:] + " --enet-smac=" +SMAC[0:] + " --infile="+ PCAP[0:] + "1" " --outfile=" + PCAP[0:] +
 "2"
os.system(cmd2)
cmd3= "tcprewrite --fixcsum --infile=" + PCAP[0:] + "2" " --outfile=" + PCAP[0:] + "-final"
os.system(cmd3)
print("The New PCAP is : " +  PCAP[0:] + "-final")
print("Cleaning temp files...")
os.system("rm -rf " + PCAP[0:] + "1")
os.system("rm -rf " + PCAP[0:] + "2")
os.system("rm -rf " + PCAP[0:] + ".cache")