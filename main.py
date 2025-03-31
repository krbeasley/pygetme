#!/opt/homebrew/bin/python3

## Get Me is intended to print some relevant info to the console

import subprocess
import socket
import argparse

GIGABYTE = 1024 * 1024 * 1024

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

intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)

def displayTime(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

def getBootTime() :
    s = subprocess.getoutput('sysctl -a | grep "kern.boottime"').split(": ")[1]

    boot = s.split(',')[0].split(" = ")[1]

    return int(boot)

def printAll():
    clear()

    print(f"USER: {USER}    MACHINE: {MACHINE}    LEAKED IP: {IP}")
    print(f"CPU: {CPU_NAME}    CORES: {CPU_CORES}    RAM: {RAM_AMT} GB")
    print(f"UPTIME: {UPTIME}")


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip_address', help='Show only the internal IP address.', action=argparse.BooleanOptionalAction)
    parser.add_argument('-u', '--user', help='Show only the current user.', action=argparse.BooleanOptionalAction)
    parser.add_argument('-t', '--uptime', help='Show the machine\'s uptime', action=argparse.BooleanOptionalAction)

    # parse arguments
    args = parser.parse_args()

    # get user
    USER = subprocess.getoutput('whoami')
    
    # get machine name
    MACHINE = subprocess.getoutput('hostname')

    # get cpu
    CPU_NAME = subprocess.getoutput('sysctl -a | grep "cpu.brand_string"').split(": ")[1]
    CPU_CORES = subprocess.getoutput('sysctl -a | grep "cpu.core_count"').split(": ")[1]

    # get ram
    RAM_AMT = str(int(subprocess.getoutput('sysctl -a | grep "hw.memsize:"').split(": ")[1]) / GIGABYTE)[0:4]

    # get local ip address
    IP = getIP()

    # get uptime
    NOW = int(subprocess.getoutput('date +%s'))
    BOOT = getBootTime()
    UPTIME = displayTime(NOW - BOOT, 4)

    # echo it all out
    if args.ip_address is None and args.user is None and args.uptime is None:
        printAll()
    else:
        if args.ip_address is not None:
            print(f"IP Address: {IP}")

        if args.user is not None:
            print(f"User: {USER}")

        if args.uptime is not None:
            print(f"Uptime: {UPTIME}")
