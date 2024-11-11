#!/opt/homebrew/bin/python3

## Get Me is intended to print somee relevant info to the console

import sys
import os
import subprocess
import socket

GIGABYTE = 1000000000

def clear() : 
    subprocess.run("clear")

def getIP() :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)

    try :
        s.connect(("123.123.123.123", 1))
        IP = s.getsockname()[0]
    except :
        IP = "127.0.0.1"
    finally :
        s.close()
    
    return IP

if __name__ == "__main__" :
    clear()

    # get user
    USER = subprocess.getoutput('whoami')
    
    # get machine name
    MACHINE = subprocess.getoutput('hostname')

    # get cpu
    CPU_NAME = subprocess.getoutput('sysctl -a | grep "cpu.brand_string"').split(": ")[1]
    CPU_CORES = subprocess.getoutput('sysctl -a | grep "cpu.core_count"').split(": ")[1]

    # get ram
    RAM_AMT = str(int(subprocess.getoutput('sysctl -a | grep "hw.memsize_usable:"').split(": ")[1]) / GIGABYTE)[0:4]

    # get local ip address
    IP = getIP()

    # get uptime


    # echo it all out
    print(f"USER: {USER}    MACHINE: {MACHINE}    LEAKED IP: {IP}")
    print(f"CPU: {CPU_NAME}    CORES: {CPU_CORES}    RAM: {RAM_AMT} GB")
