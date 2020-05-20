#!/usr/bin/env python3.7

"""Scans and Lists ports that are open on 1 System.
"""

import socket
import sys
import time
import multiprocessing

def help_section():
    print("\n***     Simple Port Scanner     ***\n")
    print("HELP Section:    -h  --help\n")
    print("Specify IP:  192.168.100.78\n")
    print("Single PORT Scanning:   -p port\n")
    print("Example: <script_name>.py 192.168.100.78 -p 80\n")
    print("Multiple PORT Scanning:   -r start end\n")
    print("Example: <script_name>.py 192.168.100.78 -r 24 80\n")
    print("This will scan IP:192.168.100.78 Starting from port 24 to port 80.\n")
    print("Scan ALL 65535 ports: -ALL. - HIGH CPU and MEMORY USAGE!!!\n")

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
    processes = []
    for port in range(start,end+1):
        p = multiprocessing.Process(target=scan, args= [port,server_info])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

def main():
    t1 = time.perf_counter()
    args = sys.argv
    argCheck = len(args)
    if argCheck == 1 and args[1] != "-h" and args[1] != "--help":
        print("\n***     WRONG ARGUMENT TRY -h or --help    ***\n")
    if argCheck > 1:
        if args[1] == "-h" or args[1] == "--help":
            help_section()
        if "-r" in args:
            argRosR = args.index("-r")
            serv = args[1]
            start_port = int(args[argRosR + 1])
            end_port = int(args[argRosR + 2])
            print("[STARTING]   Connection Test Starting...")
            test_connection()
            breaker(start_port,end_port,serv)
            t2 = time.perf_counter()
            print(f"Finished in {t2-t1} seconds.")
            sys.exit()
        if "-p" in args:
            argPosP = args.index("-p")
            serv = args[1]
            portS = int(args[argPosP + 1])
            print("[STARTING]   Connection Test Starting...")
            test_connection()
            scan(portS,serv)
            t2 = time.perf_counter()
            print(f"Finished in {t2-t1} seconds.")
            sys.exit()
        if "-ALL" in args:
            serv = args[1]
            print("[STARTING]   Connection Test Starting...")
            test_connection()
            breaker(1,65535,serv)
            t2 = time.perf_counter()
            print(f"Finished in {t2-t1} seconds.")
            sys.exit()

if __name__=="__main__":
    main()