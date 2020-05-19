# Simple Port Scanner

## HELP Section:  USE -h OR --help

Specify IP just after script name 192.168.100.78

Single PORT Scanning: -p port

Example: To scan port 80 on IP 192.168.100.78:
```
wildscanner.py 192.168.100.78 -p 80
```
Multiple PORT Scanning:  -r start end

Example: To scan port 24-80 on IP 192.168.100.78:
```
wildscanner.py 192.168.100.78 -r 24 80
```
## -ALL - HIGH CPU and MEMORY USAGE!!!

Scan ALL 65535 ports: -ALL. - HIGH CPU and MEMORY USAGE!!!
```
wildscanner.py 192.168.100.78 -ALL
```