__author__ = 'digao'
import sys
import StringIO
import re


ipv4 = '(\d{1,3})\\.(\d{1,3})\\.(\d{1,3})\\.(\d{1,3})'

def is_v4(s):
    m = re.match(ipv4,s)
    if not m:
        return False
    if m.groups():
        for _n in m.groups():
            n = int(_n)
            if n<0 or n>255:
                return False
    else:
        return False
    return True

ipv6 = '^([\da-fA-F]{1,4}):([\da-fA-F]{1,4}):([\da-fA-F]{1,4}):([\da-fA-F]{1,4}):([\da-fA-F]{1,4}):([\da-fA-F]{1,4}):([\da-fA-F]{1,4}):([\da-fA-F]{1,4})$'

def is_v6(s):
    m = re.match(ipv6,s)
    if m and m.groups():
        for _n in m.groups():
            try:
                n = int(_n,16)
            except ValueError:
                return False
    else: return False
    return True




def main(input):
    first=True
    for line in input.readlines():
        if first:
            first=False
            continue
        line = line.strip()
        if is_v4(line):
            print 'IPv4'
        elif is_v6(line):
            print 'IPv6'
        else:
            print 'Neither'



t = """3
This line has junk text.
121.18.19.20
2001:0db8:0000:0000:0000:ff00:0042:8329
1050:10:0:0:15:600:300c:326k
1050:10:0:0:15:600:300c:326g
1050:10:0:0:15:600:300c:326h
1050:10:0:0:15:600:300c:326i
"""


main(StringIO.StringIO(t))
#main(sys.stdin)