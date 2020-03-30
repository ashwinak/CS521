#!/usr/bin/python3
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

import ftplib

f = ftplib.FTP("172.19.64.160")

try:
    f.login("ashwinak", "lab1234")
    print(f.getwelcome())
    f.delete("myfile")
    print(f.dir())
    f.set_pasv(1)
    f.storbinary("STOR myfile", open("myfile", "rb"))
    print(f.dir())
except Exception as e:
    print("Exception: ", e)
finally:
    f.close()
