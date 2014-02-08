__author__ = 'digao'
from StringIO import StringIO
import sys,re
import math


def calc(i,j,x,y):
        return max(abs(i-x),abs(j-y))

def solve(numbers):
    N = len(numbers)
    mx = round(sum(a[0] for a in numbers)*1.0/N)
    my = round(sum(a[1] for a in numbers)*1.0/N)
    S = sum([calc(mx,my,a[0],a[1]) for a in numbers])
    return int(S)


def main(input):
    N=None
    numbers = []
    for line in input.readlines():
        if not line:continue
        if N is None:
            N = int(line)
        else:
            x,y = map(int,line.strip().split())
            numbers.append((x,y))
    print solve(numbers)


test_input = """6
12 -14
-3 3
-14 7
-14 -3
2 -12
-1 -6"""

main(StringIO(test_input))
#main(sys.stdin)