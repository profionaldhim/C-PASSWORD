 #!bin/python
import os
import random
import sys
import time

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray
print('\033[0m=================================================================================')
os.system('figlet -f mono9.tlf "C-Password" ')
print('\033[32m')
m = "THIS TOOL TO CREATE STRONG PASSWORD FOR YOUR ACCOUNT ©"
print(m)
t = "Copy®ight Mohammed Info wh :- +967733014747"
print(t)
y = " FROM :- YEMEN"
print(y)
print('\033[0m================================================================================')
print('\033[32m ~~ wellcome in my tool to create password ~~')
menu = [ "{-1-} Start Create Password", "{-0-} Exit [~]" ]
print (menu [0])
print (menu [1])
number = int(input('Enter number:: '))
if number == 0:
 os.system('figlet -f mono12.tlf "Good Bye" ')
 os.system('exit')
# break
# else:
 #  print('negative number')
elif number == 1:
     print('Please Insert count littles or number ?')
    #aaa=input('\033[1;33mEntre Your Name : \033[1;32m')
     num_box = int(input('Enter number :: '))
     #number2 = int(input('Enter number:: ')) 
     print('please insert your name ?')
     nam_your = input('Enter your name:: ')
     print('please insert your phone ?')
     phone = int(input('Enter number:: '))
     print('please insert your date birthday ex : 1/1/1990 =111990 ?')
     date_u = int(input('Enter number:: '))
     naa = phone - date_u 
     nu1 = naa * 2 
    #total = nu1 + 99999999999
     total = nu1
     def my_function(fname):
       print(nam_your,+fname)
     print('Your Password ===>')
     my_function(total)
     s = len(nam_your)
     q = len(str(total))
     dat = len(str(date_u))
     phone_u = len(str(phone))
     uu = len(str(nu1))
     tt = s + uu 
     f = tt
     print('Length of Password',f)
     if f > 16:
      print('\033[32m Nice Password ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
      men2 = ["{-00-} Back"]
      print(men2 [0])
      m2 = int(input('Enter number :: '))

      if m2 == 00:
       os.system('clear')
       os.system('python c-password.py')
      # else:
       #print('Nothing')
     elif f == 16:
      print('\033[33m Normal Password ▄▄▄▄▄▄▄▄▄▄▄▄')
      men3 = ["{-00-} Back"]
      print(men3 [0])
      mmm3 = int(input('Enter number :: '))

      if mmm3 == 00:
       os.system('clear')
       os.system('python c-password.py')
       #else:
       #print('Nothing')
     elif f < 16:
      print('\033[31m weak Password ▄▄▄▄▄▄▄')
#     else:
 #     print('Nothing')
 
      me = ["{-00-} Back"]
      print(me [0])
      mmm = int(input('Enter number :: '))
 
      if mmm == 00:
       os.system('clear')
       os.system('python c-password.py')
       #else:
       #print('Nothing')

    #elif number == 2:
      #print('one')
      #elif number == 3:
      #print('three')
#elif number == 0:
 #os.system('figlet -f mono12.tlf "Good Bye" ')
 #os.system('exit') 
# break
#else:
#   print('negative number')


