#! /usr/bin/python
from fractions import Fraction

count = 0
try:
    for n in range(1,2015):
        for m in range(1,n):
            for p in range(1,m):
                if (Fraction(1,n)+Fraction(1,3)==Fraction(p,m)):
                    count=count+1
                    print "n=",n," m=",m," p=",p
except KeyboardInterrupt:
    print "\n" \
          "User exited program..."
print count