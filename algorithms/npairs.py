__author__ = 'digao'
from StringIO import StringIO
import sys


def solve(array,K):
    N = len(array)
    ss = set(array)
    counter = 0
    for a in array:
        if (a+K) in ss:
            counter += 1
    return counter



def main(input):
    N=None
    K=None
    for line in input.readlines():
        if N is None:
            N,K = map(int,line.strip().split())
        else:
            print solve(map(int,line.strip().split()),K)

test_input = """5 2
1 5 3 2 4
"""

main(StringIO(test_input))
#main(sys.stdin)