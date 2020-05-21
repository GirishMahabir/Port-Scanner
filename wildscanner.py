#!/usr/bin/env python3.7

"""Scans and Lists ports that are open on 1 System.
"""

import socket
import sys
import time
import argparse
import threading

def get_args():
    parser = argparse.ArgumentParser(description='Port Scanning.')
    parser.add_argument('IP',help='Specify IP.')
    parser.add_argument('-p',default=None,help='Specify the port.')
    parser.add_argument('-r',default=None,help='Specify range of ports 1000-2000 or supply ALL to scan ALL(65535) ports.')
    args = parser.parse_args()
    return args

def test_connection(host='google.com',port=80):
    try:
        socket.create_connection((host,port), 2)
        print("We are ready to scan your desired server.")
    except OSError:
        print("An OS error has been encountered.")

def scan(port,server_info):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((server_info,port))
        if result == 0:
            print(f"Port {port}: OPEN")
    except socket.gaierror:
        print("Host could not be resolved")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()
    finally:
        sock.close()

def breaker(start,end,server_info):
    for port in range(start,end+1):
        x = threading.Thread(target=scan, args= (port,server_info,))
        x.start()

def main():
    args = get_args()
    t1 = time.perf_counter()
    if args.p != None:
        print("[STARTING]   Connection Test Starting...")
        test_connection()
        scan(int(args.p),args.IP)
        t2 = time.perf_counter()
        print(f"Finished in {t2-t1} seconds.")
        sys.exit()
    if args.r != None and args.r != "ALL":
        portList = args.r.split("-")
        print("[STARTING]   Connection Test Starting...")
        test_connection()
        breaker(int(portList[0]),int(portList[-1]),args.IP)
        t2 = time.perf_counter()
        print(f"Finished in {t2-t1} seconds.")
        sys.exit()
    if args.r == "ALL":
        print("[STARTING]   Connection Test Starting...")
        test_connection()
        breaker(1,65535,args.IP)
        t2 = time.perf_counter()
        print(f"Finished in {t2-t1} seconds.")
        sys.exit()

if __name__=="__main__":
    main()