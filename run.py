#!/usr/bin/env python3

import os
import sys
import time

def lowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)

memu1 = ('''\033[1;33;40m
 ___________________________
|                             |
|                             | 
|           1 RUN             |
|           2 SETUP           |
|           4 CR              |
|           5 UPDATE          |
|          99 EXIT            |
|                             |
|_____________________________|

''')

memu2 = ('''\033[1;33;40m
 ___________________________
|                             |
|                             | 
|       1 SETUP TERMUX        |
|       2 SETUP SHELL         |
|       3 SETUP UBUNTU        |
|       4 SETUP KALI LINUX    |
|      99 EXIT                |
|                             |
|_____________________________|

''')

cr=('''\033[0;32m
╦═╗ ╦╦ ╦╔═╗╔═╗╦╔═╦ ╦╔═╗╦ ╦
╠╦╝ ║╠═╣╠═╣║  ╠╩╗╚╦╝║ ║║ ║
╩╚═╚╝╩ ╩╩ ╩╚═╝╩ ╩ ╩ ╚═╝╚═╝ o
=================================
Project จัดทำโดย Sakol Thaneerat ได้ดัดเเปลง ทำเพื่อเป็น Tool ในการใช่ DIRB ได้ง่ายขึ้น 
''')

xr=("______________________________________________________")

os.system("clear")
lowprint(memu1)
x = input("number : ")
if x == "1":
    os.system("clear")
    input1 = input("link : ")
    input2 = input("name-word-list: ")
    os.system("dirb  %s  -w  %s " %(input1, input2))    
if x == "2":
    os.system("clear")
    lowprint(memu2)
    q = input("setup : ")
    if q == "1":
        print("termux")
        os.system("clear")
        os.system("pkg install dirb")
        os.system("apt install dirb")
        os.system("clear")
        time.sleep(2.0)
        os.system("python3 run.py")
    if q == "2":
        print("shell")
        os.system("sudo apt install dirb")
        os.system("clear")
        time.sleep(2.0)
        os.system("python3 run.py")
    if q == "3":
        print("ubuntu")
        os.system("sudo apt install dirb")
        os.system("clear")
        time.sleep(2.0)
        os.system("python3 run.py")
    if q == "4":
        print("kali")
        print("kali not setup")
        os.system("clear")
        time.sleep(2.0)
        os.system("python3 run.py")
    if q == "99":
        print("exit")
        os.system("clear")
        time.sleep(2.0)
        os.system("exit")
if x == "4":
    os.system("clear")
    lowprint(cr)
    lowprint(xr)
    time.sleep(1.0)
    w = input("Enter...: ")
    os.system("python3 run.py")
if x == "5":
    os.system("clear")
    os.system("git pull https://github.com/sakol289/dirb/")
    os.system("python3 run.py")
if x == "99":
    os.system("exit")
# else:
#     os.system("python3 run.py")