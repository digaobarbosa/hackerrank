__author__ = 'digao'
from StringIO import StringIO
import sys,re

ip = '\(\+?\-?(\d{1,3}\.?\d*),\s*\+?\-?(\d{1,3}\.?\d*)\)'

def solve(line):
    m = re.match(ip,line)
    if m is None: return False
    lat = m.group(1)
    lat = (lat[0]!='0' and lat[-1]!='.') and float(lat) or None
    long = m.group(2)
    long = (long[0]!='0' and long[-1]!='.') and float(long) or None
    return lat and long and lat>=-90 and lat<=90 and long>=-180 and long<=180 and 'Valid' or 'Invalid'

def main(input):
    N=None
    for line in input.readlines():
        if N is None:
            N=True
        else:
            print solve(line.strip())

test_input = """12
(-090.00000, -180.0000)
(90., 180.)
(75, 180)
(+90.0, -147.45)
(77.11112223331, 149.99999999)
(+90, +180)
(90, 180)
(-90.00000, -180.0000)
(75, 280)
(+190.0, -147.45)
(77.11112223331, 249.99999999)
(+90, +180.2)"""

main(StringIO(test_input))
#main(sys.stdin)