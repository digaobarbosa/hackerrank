__author__ = 'digao'
from StringIO import StringIO
import sys

cache = [1]

def solve(money,p,disc):
    sum = wrappers = money/p
    while wrappers>=disc:
        div = wrappers/disc
        sum+=div
        wrappers = div + wrappers%disc
    return sum

def main(input):
    N=None
    for line in input.readlines():
        if N is None:
            N = int(line.strip())
        else:
            print solve(*map(int,line.strip().split()))

test_input = """3
10 2 5
12 4 4
6 2 2
"""

main(StringIO(test_input))
#main(sys.stdin)