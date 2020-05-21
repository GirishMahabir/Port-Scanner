# Simple Port Scanner

## Help Section: -h OR --help
```
wildscanner.py -h
wildscanner.py --help
```
Specify IP just after script name 192.168.100.78

Single PORT Scanning: -p port

Example: To scan port 80 on IP 192.168.100.78:
```
wildscanner.py 192.168.100.78 -p 80
```
Multiple PORT Scanning:  -r start end
The - is important!
Example: To scan port 24-80 on IP 192.168.100.78:
```
wildscanner.py 192.168.100.78 -r 24-80
```
## ALL
Scan ALL 65535 ports:
ALL should be all UPPERCASE.
```
wildscanner.py 192.168.100.78 -r ALL
```