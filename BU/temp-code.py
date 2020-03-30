#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:47:53 2019

@author: ashwinak
"""


#set2=set(dict1)
#set2.add(dict1.values())
#print(type(set2))
#print(set2)



#list1 = []
#for k,v in dict1.items():
#    #values = dict1.values(v)
#    set1 = set(dict1.values())

#print(set1)
#list1 = list(set1)
#set2=set()
#for k,v in dict1.items():
#    i=0
#    list2 = []
#    while i < len(list1):
#        if list1[i] == v:
#            #print (list1[i],"members are",k)
#            set2.add((list1[i]))
#            print(set2)
#            i+=1
#        else:
#            continue

# Unused Code.
#file_read = open(in_file,"r")
#rawCSV = dict1.read().split(",")
#print (rawCSV)
#print([x[::2] for x in rawCSV if 'parent_ae_name' in x])

#with open ('parent_ae_name.csv', 'r') as f:
#    file=f.read()
#    while "interfaces/interface/" in file:
#        file = file.replace("interfaces/interface/", '')
#        file = file.replace("/state/parent_ae_name", '')
#with open('parent_ae_name.csv', "w") as f:
#    f.write(file)


#with open ('stats1.txt') as iFile,open('parent_ae_name.csv', 'w') as oFile:
#    for line in iFile:
#        if ("parent_ae_name, ae" in line):
#            oFile.write(line)
#        elif ("parent_ae_name,ae" in line):
#            oFile.write(line)
#        else:
#            continue
    
#list_in_pkts = []
#with open('in-pkts.csv') as csv_file:
#    reader = csv.reader(csv_file,delimiter=',')
#    i=0
#    while i < len(list_ae_names):
#        ae = list_ae_names[i]
#        #print(dict_ae_members['list_%s' % ae])
#        for items in (dict_ae_members['list_%s' % ae]):
#            #print (items)
#            for row in reader:
#                for column in row:
#                    if column==items:
#                        list_in_pkts.append(int(row[1]))
#                        #print("In",list_in_pkts)
#        print("out",list_in_pkts)
#        i+=1

#i=0
    
#while i <len(list_ae_names):
#    ae = list_ae_names[i]
#    #print(dict_ae_members['list_%s' % ae])
#    j=0
#    while j < len(dict_ae_members['list_%s' % ae]):
#        with open('in-pkts.csv') as csv_file:
#            reader = csv.reader(csv_file,delimiter=',')
#            for row in reader:
#                for column in row:
#                    if column==dict_ae_members['list_%s' % ae][j]:
#                        cnt = int(row[1])
#                        list_in_pkts.append(cnt)
#                    print(list_in_pkts)
##                    else:
##                        continue
#        j+=1
#    i+=1
#        
#    

#
#json_body = [
#    {
#        "measurement": "Traffic_stats",
#        "tags": {
#            "host": "xe-8/0/0",
#            "region": "us-west"
#        },
#        "time": current_time,
#        "fields": {
#            "Int_value": 293687,
#        }
#    }
#]        
#  
#
#                        timestamp = int(timestamp) + 1
#                        timestamp = str(timestamp)
#                        #current_time = current_time + datetime.timedelta(0,3)
#                        #sleep(0.001)
##                        print("before",current_time)
#                        #current_time = current_time + timedelta(seconds=2)
#                        current_time = current_time + 1000
##                        print("after",current_time)
#                        #current_time = datetime.datetime.now()
#                        #current_time.strftime('%Y-%m-%dT%H:%M:%SZ') #2018-03-28T8:01:00Z



# to take TS from in_file.            
#    with open (in_file) as iFile,open("ts.csv", 'w') as oFile:
#        for line in iFile:
#            if ('__timestamp__' in line):
#                oFile.write(line)
#    with open('inPkts.csv') as csv_file,open("ts.csv", 'a+') as oFile:
#        reader = csv.reader(csv_file,delimiter=',')
#        for row in reader:
#            for column in row:
#                if (column not in line):
#                    oFile.write(line)
#
#
#
#Video: 5 minute overview of the project
#
#
#(1)  at least one of the container types (list, tuple, set, or dictionary)
#(2)	 at least one iteration type (for, while)
#(3)	 at least one conditional
#(4)	 at least one user-defined function
#(5)	 at least one user-defined class (could be very simple)
#(6)	 file input or output
#
#Given a CSV file that has the following data, plot graph for interface counters and aggregate interface counters based on parent AE name.
#
#X-axis:
#interfaces/interface/xe-8/1/1/__timestamp__, 1550369868935
#interfaces/interface/xe-8/1/1/state/parent_ae_name,ae21--->
#interfaces/interface/xe-8/1/1/state/high-speed, 10000
#
#Y-axis:                                                                                     
#interfaces/interface/xe-8/1/1/state/counters/in-pkts, 3157643
#interfaces/interface/xe-8/1/1/state/counters/in-octets, 1361231350
#interfaces/interface/xe-8/1/1/state/counters/in-unicast-pkts, 415524
#interfaces/interface/xe-8/1/1/state/counters/in-multicast-pkts, 2738935
#interfaces/interface/xe-8/1/1/state/counters/in-broadcast-pkts, 3188
#interfaces/interface/xe-8/1/1/state/counters/out-pkts, 911488235
#interfaces/interface/xe-8/1/1/state/counters/out-octets, 427841745512
#interfaces/interface/xe-8/1/1/state/counters/out-unicast-pkts, 901459835
#interfaces/interface/xe-8/1/1/state/counters/out-multicast-pkts, 10025189
#interfaces/interface/xe-8/1/1/state/counters/out-broadcast-pkts, 3202
#
#Results:
#Display graphs for each inteface (Label: xe-8/1/1 or ae21) from the CSV.
#Display hot links i.e links carrying traffic close to its capacity.
#Display links carrying errors frames.
#
#Algorithm:
#
#> Store the KV pairs to a dictionary or sets.
#    
#> Read the CSV file and create another file with: dict_parent_ae_name
#    k = IFD name
#    v = Counter value
#> when "parent_ae_name" is not empty:  dict2
#    k = IFD name
#    v = AE name
#> From dict2 find IFD's which has same values.
#> Use the IFD's found from previous step and find and aggregate its values from dict_parent_ae_name.
#> Display the aggregate result but:
#    k = AE name
#    v = aggregated value.
#> use influxdb API to plot the above data.
#        
    
    