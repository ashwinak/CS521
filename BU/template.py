# class Solution:
#     def twoSum(self, nums, target):
#         seen = {}
#         for i, v in enumerate(nums):
#             remaining = target - v
#             if remaining in seen:
#                 return [seen[remaining], i]
#             seen[v] = i
#         return []
# S = Solution()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:50:32 2020

@author: ashwinak
"""

#write a for loop to print elements in list and their positions


# x = ['M','o','z','z','a','r','e','l','l','a'] 

# for c,d in enumerate(x):
#     print(c,d)


# #find dups in a list and set variable to true if dupe exist, else false.

# plist =[1,2,3,3,4,5,6,6]

# has_dups = None
# for idx in range(len(plist)):
#     if plist[idx]==plist[idx+1]:
#         has_dups == True
#     else:
#         has_dups == False
        
        
        
# plist2 = ['A','s','h','w','i','n']
# plist = []
# for item in plist2:
#     plist.append(item.upper())
# print(plist)


# x_list = [5, 7, 8, -9, 4, -5]
# y_list = [x + 1 for x in x_list if x > 0]
# print(y_list)       

# x = [1,3,8,3,6,8,11,19,22]

# x_even = []
# x_odd = []
# for i in range(len(x)):
#     if i%2 == 0:
#         x_even.append(i)
#     else:
#         x_odd.append(i)

# print(x_even)
# print(x_odd)


# n = [1,2,5,10,3,100,9,24]
# m = []
# for e in n: 
#     if e >= 5:
#        m.append(e)
#     print (m)


# y = [1, 13, 61, 99, 17,18,23,35,88,99]
# print(y)
# x = int(input("Enter an element from the above list of numbers: "))

# for i,v in enumerate(y):
#     if v == x:
#         print (y[-abs(i)-1])


# import sys
# current_members = [1, 13, 61, 99, 17,18,23,35,88,99]

# member_id = int(input("Enter an element from the above list of numbers: "))

# is_a_member = None
# for i,v in enumerate(current_members):
#     if v == member_id:
#         is_a_member = True
#         print("Member ID exist")
#         sys.exit()
# print("Member ID does not exist.")
    
        
# try:
#     zipcode_list = [1, 13,13, 61, 99, 17,18,23,35,88,99]
#     duplicates = None
#     for i,k in enumerate(zipcode_list):
#         if zipcode_list[i] == zipcode_list[i+1]:
#             duplicates == True
#             print("Duplicate exist at index ", i)
#         else:
#             duplicates == False
#             print("Duplicate does not exist at index ", i)
# except IndexError as error:
#     print("End of list reached: ",error)




# try:
#     zipcode_list = [1, 13,12, 61, 99, 17,18,14,35,11,55]
#     duplicates = None
#     print(len(zipcode_list))
#     print(len(set(zipcode_list)))
#     if len(zipcode_list) == len(set(zipcode_list)):
#         duplicates == True
#         print("Duplicate does not exist")
#     else:
#         duplicates == False
#         print("Duplicates exist")
# except IndexError as error:
#     print("End of list reached: ",error)





# try:
#     incompletes = [1,13,12,61,13,17,13,14,35,11,55]
#     student_id = int(input("Enter student_id: "))
#     number_of_incompletes = 0
#     for i in incompletes:
#         if student_id == i:
#             number_of_incompletes = number_of_incompletes + 1
#     print("Number of incompletes is: ",number_of_incompletes)
    
# except IndexError as error:
#     print("End of list reached: ",error)
    
    
    
# list1 = [1,2,3,6,8,7,9]
# list2 = [4,5,6,7,8]

# if len(list1) < len(list2):
#     l1 = len(list2) - len(list1)
#     pad = [None] * l1
#     list1 = list1 + pad
#     print(list1)
# else:
#     l1 = len(list1) - len(list2)
#     pad = [None] * l1
#     list2 = list2 + pad
#     print(list2)

# list3 = list(zip(list1,list2))
# # list.reverse(list3)
# print(list3)
# list4 = []
# for i in range(len(list3)):
#     list4.append(list3[i][0])
#     list4.append(list3[i][1])
# res = [i for i in list4 if i]
# print(res)
    
    
    
    
    
# n = int(input("Enter n: "))
# d = 2
# list1 = []
# for i in range(n):
#     if i == 0:
#         continue 
#     else:
#         list1.append(i)
# print(list1[0:len(list1):d])


# m = int(input("Enter m: "))
# n = int(input("Enter n: "))
# d = 2
# list1 = []

# for i in range(n):
#     list1.append(i)
    
# print(list1[m:n:d])


# n = int(input("Enter n: "))
# r = int(input("Enter r: "))
# list1 = []
# list1.append(1)
# # print(list1)
# for i,j in enumerate(list1):
#     if j > n:
#         list1.remove(j)
#         break
#     elif j == n:
#         break
#     else:
#         list1.append(j*r)
# print(list1)  



# n = int(input("Enter n: "))
# list1 = []
# list1.append(0)
# list1.append(1)
# # print(list1)
# r = 0
# for i,j in enumerate(list1):
#     if r > n:
#         list1.remove(r)
#         break
#     elif r == n:
#         break
#     else:
#         r = list1[i] + list1[i+1]
#         list1.append(r)
# print(list1)  


# n = int(input("Enter n: "))
# m = int(input("Enter m: "))

# list1 = []
# list1.append(0)
# list1.append(1)
# # print(list1)
# r = 0
# for i,j in enumerate(list1):
#     if r > n:
#         list1.remove(r)
#         break
#     elif r == n:
#         break
#     else:
#         r = list1[i] + list1[i+1]
#         list1.append(r)
# list2 = []  
# for i,j in enumerate(list1):
#     if j<m:
#         list2.append(j)
# print([item for item in list1 if item not in list2])


# list1 = [4,3,2,6,2]
# list2 = [1,2,4]
# list3 = [item for item in list1 if item in list2]
# print(sorted(list3))




# list1 = [4,3,2,6,2]
# list2 = [1,2,4,1,5]
# list3 = [item for item in list1 if item not in list2]
# list4 = [item for item in list2 if item not in list1]
# list5 = [item for item in list1 + list2 ]
#print(list5)
# print(sorted(list3 + list4))

# print(len(sorted(list3 + list4)))

# list2.append(5)
# print(list2)
# k = list2.pop(-1)
# print(list2)
# list2.pop(3)
# print(list2)
# print(k)


# list1 = [4,3,2,6,2,8,7,6,3,4,9]
# list2 = [1,2,4,1,5]

# k = 0
# for i,j in enumerate(list1):
#     if (i >=5 and i<=8):
#         m = list2[k]
#         list1[i] = m
#         k+=1
# print(list1)
    
# import math
# total = 0
# for k in range(1,50):
#     total = total + math.pow(k,2)
#     print(total)
# print(total)


# import math
# total = 0
# n = 20
# for k in range(1,n):
#     total = total + math.pow(k,3)
#     print(total)
# print(total)


# import math
# total = 0
# k = 0
# while k <50:
#     total = total + math.pow(k,2)
#     k+=1
#     print(total)
# print(total)    


# import math
# h = 19
# k = 1
# q = 0
# q1 = []
# while k <=h:
#     q = math.pow(k,2)
#     k+=1
#     if q >= h:
#         break
#     q1.append(q)
# print(len(q1))
# print(q1)

# h = 40
# m = 10
# k = 1
# q = 0
# q1 = []
# while k <=h:
#     q = k * k
#     k+=1
#     if q<=m:
#         continue
#     elif q >= h:
#         break
#     else:
#         pass
#     q1.append(q)
# print(len(q1))
# print(q1)

# import sys
# n = 11

# for i in range(2,n):
#     if (n % i) == 0:
#         print(n, " is not a prime number")
#         sys.exit()
# print(n, " is a prime number")


# x = 'malayalam'
# for i,v in enumerate(x):
#     # print(i,v)
#     if i ==8:
#         break
#     if x[i] == x[i+1]:
#         print (x[i])
        
# # print (i, "is the first repeating char")

# wd = ['abc', 'def', 'abc']

# for i in wd:
#     cnt = wd.count(i)
    
#     print (i,cnt, "times")
        
        
# d = {'one':1,'two':2}
# inverse = dict()
# print(type(d.items()))
# inverse = {v:k for k,v in d.items()}

# print(type(inverse))
# print(inverse)

# d = {5:3,10:4,12:1}
# maxi = max(d.keys())
# print(d[maxi])

# d1 = {2:3,8:19,6:4,5:12}
# d2 = {2:5,4:3,3:9}
# d1rev = {v:k for k,v in d1.items()}                
# d3 = {}
# for j,v in d1rev.items():
#     try:
#         d3[d1rev[j]] = d2[j]
#     except KeyError:
#         pass
# print(d3)


# d1 = {2:3,8:19,6:4,5:12}
# d2 = {2:5,4:3,3:9}

# d1key = list(d1.keys())
# d2key = list(d2.keys())
# d1keys = list(set(d1key) - set(d2key))
# d2keys = list(set(d2key) - set(d1key))
# d3 = {}


# for i,k in enumerate(d1keys):
#     d3[k] = d1[k]
# for l,m in enumerate(d2keys):
#     d3[m] = d2[m]
# print(d3)

# d = {1:2,3:4,5:6,7:8}
# lst = [1,7]
# d1 = d.copy()
# for i,j in enumerate(lst):
#     del d1[j]
# print(d1)
# print(d)
    
# d = {'yxz':4,'abc':1,'def':2,'ghi':3}

# lst = sorted(d.keys())
# d1 = {}
# for i,j in enumerate(lst):
#     d1[j] = d[j]
# print(d1)    


# d = {'ash':'dmk', 'viru': 'admk', 'avi': 'congress', 'shiva' : 'dmk','anand':'congress'}

# lst = list(d.values())

# d1 = {}
# for i in lst:
#     d1[i] = lst.count(i)
# print(d1)    



# d3 = {'ash': 1000, 'win': 2000, 'ram': 500}
# m = list(d3.values())

# m1 = max(m)

# for k,v in d3.items():
#     if d3[k] == m1:
#         print(k, "is the winner with # of votes", d3[k])
        


    
# t = (1,6,5,7,1,3,4,1)
# for i in t:
#     repeats = t.count(t[0]) - 1
# print(repeats)

## Find closest number from a list of ints.
    
# wt = {12,19,6,14,22,7}
# K = 18
# lst = list(wt)
# actual_wt = lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

# wt.remove(actual_wt)

# print(actual_wt)
# print(wt)


# s = 'pandemic'

    
# s1 = 'hello'

# s2 = 'world'
# s3 = ""
# for i,v in enumerate(s1):
#     s3 = s3 + s1[i] + s2[i]
# print(s3)    


# s1 = 'hello'
# s2 = 'world'
# s11 = s1[::-1]
# s22 = s2[::-1]
# s3 = ""
# for i,v in enumerate(s11):
#     s3 = s3 + s11[i] + s22[i]
# print(s3) 


# s1 = 'hel'

# s2 = 'worlds'
# s3 = ""
# for i,v in enumerate(s1):
#     s3 = s3 + s1[i] + s2[i]
# print(s3)     


# s1 = 'helllllo'
# s2 = 'worlds'
# s3 = ""

# if len(s1) > len(s2):
#     ls = len(s1) - len(s2)
#     s2 = s2 + ls * " "
#     for i,v in enumerate(s1):
#         s3 = s3 + s1[i] + s2[i]
# else:
#     ls = len(s2) - len(s1)
#     s1 = s1 + ls * " "
#     for i,v in enumerate(s2):
#         s3 = s3 + s1[i] + s2[i]
# print(s3.replace(" ",""))    

# t = ('abc','def','ghij','pand','blah','blah')

# i = 0
# four_letter_word_count = 0
# while i < len(t):
#     if len(t[i]) == 4:
#         four_letter_word_count+=1
#     i+=1


# print("No of 4 letter word counts is",four_letter_word_count)
        
# s = ""        

# i = 0
# while i < 777:
#     s = s + "*"
#     i+=1
# print(s)
# print(len(s))


# s = ""        

# i = 0
# n = 4
# while i < 2 * n :
#     s = s + "*"
#     i+=1
# print(s)
# print(len(s))


# s = 'hellllloaeiou'

# i = 0
# vowel_count = 0
# while i < len(s):
#     if any([s[i]=='a',s[i]=='e',s[i]=='i',s[i]=='o',s[i]=='u']):
#             vowel_count +=1
#     i+=1
# print(vowel_count)    

# import re
# email = 'blah@blah.'
# if re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',email):
#     print("True")
# else:
#     print("false")



lst = ['abc\n','def\n','ghi\n']

f_name = "test.txt"
txt = open(f_name,"w")

txt.writelines(lst)
txt.close()

import os

# if os.path.exists('test.txt'):
#     print("File exist")
# else:
#     print("File does not exist")

# if os.path.isfile('test.txt'):
#     print("This is a file")
# else:
#     print("This is not a file")
    
# if os.path.isdir('test.txt'):
#     print("This is a dir")
# else:
#     print("This is not a dir")
        

# f_name = "test.txt"
# txt = open(f_name,"r")

# for i in reversed(list(txt)):
#     print(i.rstrip())

# txt.close()
    
# import os

# if os.path.exists('test.txt'):
#     print("File exist")
# else:
#     print("File does not exist")
# os.remove('test.txt')    

# if os.path.exists('test.txt'):
#     print("File exist")
# else:
#     print("File does not exist")



# f_name = "test.txt"
# txt = open(f_name,"r")

# for i in txt:
#     print(len(i.rstrip()))
# txt.close()



# def is_prime(x):
#     for i in range(2,x):
#         if (x % i) == 0:
#             return False
#     return True


# # print(is_prime(0))

# n = 20

# lst = []

# for i in range(20):
#     if is_prime(i) is True:
#         lst.append(i)
# total = (sum(lst))
# print(lst,total)
# print(len(lst))
# k=0
# for j in range(2,len(lst)):
#     k+=1

# print(k)       
    



# def typing_speed(nw,t):
#     tspeed = (nw / t) * 60
#     return tspeed

# speed = int(input("Enter number of words typed: "))
# interval = int(input("Enter the time interval in seconds: "))
# print("")
# print("Typing speed per minute is",round(typing_speed(speed,interval),3), "words")


# def send_variable(x:int):
#     if not isinstance(x, int):
#         raise TypeError
#     return True 

# x = 10

# print(send_variable(x))


# class customer:
#     def __init__(self,name):
#         self.name = name 

# a = customer('Meg_Ash')
# print(type(a))
# x = 10
# print(type(x))

# def send_variable(x:customer):
#     if not isinstance(x, customer):
#         raise TypeError
#     return True 

# b = 'abc'
# print(send_variable(a))
    
    
# def min(x,y,z):
#     if ord(x[0]) < ord(y[0]) and ord(x[0]) < ord(z[0]):
#         return x
#     elif ord(y[0]) < ord(x[0]) and ord(y[0]) < ord(z[0]):
#         return y
#     else:
#         return z

# print(min('a','B','A'))
# # print(min('Meghna','Ashwin','Shiva'))
    

# def add(x,y):
#     return(x+y)

# euro_Sales = 1000
# asia_Sales = 100

# eurasia_Sales = add(euro_Sales, asia_Sales)

# print(eurasia_Sales)


# def to_the_power_of(x,y):
#     return max(x,y)

# cube_volume = to_the_power_of(6, 3)
# print(cube_volume)


# def send_variable(x,y):
#     '''
#     x is double precision float
#     y is int.

#     '''
#     if not isinstance(x, float):
#         raise TypeError
    
#     if y < 0:
#         return 0
#     else:
#         return(x**y)
    
# print(send_variable(2.2, 2))


# class AirConditioner():
#     def __init__(self):
#         self.State = 0
#         self.Temp = 0
    
#     def turnOn(self,State=1):
#         self.State = 1
#         return True
    
#     def turnOff(self,State=0):
#         self.State = 0
#         return True

#     def setTemp(self,Temp):
#         self.Temp = Temp
        
#     def getTemp(self):
#         return self.Temp
    
#     def isOn(self):
#         if self.State == 1:
#             return True
#         else:
#             return False

#     def isOff(self):
#         if self.State != 1:
#             return True
#         else:
#             return False

        
# my_ac = AirConditioner()

# print("Turn on AC")
# my_ac.turnOn()
# print("Set temperature ")
# my_ac.setTemp(72)
# print("Get temperature ")
# print(my_ac.getTemp())
# print(my_ac.isOff())
# print(my_ac.isOn())

# office_a_c = AirConditioner()

# office_a_c.turnOn()
# office_a_c.setTemp(69)

        
# class Counter():
#     def __init__(self):
#         self.counter = 0
#         self.limit = 2       
    
#     def increment(self,counter=0):
#         if self.counter < self.limit:
#             self.counter +=1
#         else:
#             pass

#     def decrement(self,counter=0):
#         if self.counter > 0:
#             self.counter -=1
#         else:
#             pass        
    
#     def getValue(self):
#         return self.counter
        
       
# obj = Counter()


# print(obj.getValue())
# obj.increment()    
# print(obj.getValue())
# obj.increment()
# print(obj.getValue())
# obj.increment()
# print(obj.getValue())

# print(obj.getValue())
# obj.decrement()    
# print(obj.getValue())
# obj.decrement()
# print(obj.getValue())


# class Player():
    
#     name = ''
#     score = 0

#     def set_name(self,name):
#         self.name = name

#     def set_score(self,score):
#         self.score = score

#     def get_name(self):
#         return self.name

#     def get_score(self):
#         return self.score

    
    
# member = Player()
# member.set_name('Ashwin')
# member.set_score(100)


# print(member.get_name())
# print(member.get_score())

    






