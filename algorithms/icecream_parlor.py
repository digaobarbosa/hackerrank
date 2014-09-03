__author__ = 'digao'
from StringIO import StringIO
import sys

def solve(money,array):
    mm = {}
    for i in xrange(len(array)):
        c = array[i]
        ind = mm.get(c)
        if ind is not None:
            return (ind+1,i+1)
        mm[money-c] = i
    return None

def main(input):
    N = int(input.readline().strip())
    for i in xrange(N):
            money = int(input.readline().strip())
            N = int(input.readline().strip())
            C = map(int,input.readline().strip().split())
            print "%d %d"%solve(money,C)

test_input = """2
4
5
1 4 5 3 2
4
4
2 2 4 3
"""

main(StringIO(test_input))
#main(sys.stdin)