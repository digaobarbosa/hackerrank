__author__ = 'digao'
import sys
import StringIO
import re


ipv4 = '^hackerrank.*'

def start_with(s):
    return re.match(ipv4,s)

ipv6 = '^.*hackerrank$'

def end_with(s):
    return re.match(ipv6,s)


def main(input):
    first=True
    for line in input.readlines():
        if first:
            first=False
            continue
        line = line.strip()
        s = start_with(line)
        e = end_with(line)
        if s and e:
            print 0
        elif s:
            print 1
        elif e:
            print 2
        else:
            print -1


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