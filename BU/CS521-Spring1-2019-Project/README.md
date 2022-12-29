```
Created on Sat Mar  9 20:06:10 2019

@author: ashwinak
```

# STEP1: Install influxdb using the below documentation:

https://www.influxdata.com/blog/getting-started-python-influxdb/

## Once installation is complete, start the influxdb from a terminal before executing the python code:
```
$ influxd -config /usr/local/etc/influxdb.conf
```

## Check if the influxdb port is in listen mode based on your base operating system:

## For MAC: 
```

$ lsof -i :8086
COMMAND   PID     USER   FD   TYPE            DEVICE SIZE/OFF NODE NAME
influxd 46194 ashwinak   29u  IPv6 <snip>.           0t0  TCP *:8086 (LISTEN)
```

# STEP2 : Install Pandas for python3.
```
$ pip3 install pandas
```
# STEP3: To run the code:
```
>python3 main.py
Enter the raw CSV log file: cs521-stats.txt
Writing data to influxdb...
```

# STEP4: Install Grafana using the below documentation for graphical view.

http://docs.grafana.org/installation/
