__author__ = 'digao'
from StringIO import StringIO
import sys

def solve():

def main(input):
    N=None
    count = 0
    for line in input.readlines():
        if N is None:
            N = int(line.strip())
        else:
            if count%2==1:
               print solve(map(int,line.strip().split()))
            count+=1

test_input = """2
3
1 3 2
5
5 3 2 1 4
5
5 2 3 4 1
5
2 3 4 5 1
5
1 3 4 5 2
5
5 4 1 2 3
"""


main(sys.stdin)
#test()
#print '------------------'
#main(StringIO(test_input))


a_test_input = """2
3
1 3 2 -> 1 2 A
5
5 3 2 1 4 -> 3 2 1 4 -> 3 2 1 -> 2 1 -> 1 B
5
5 2 3 4 1 -> 5 2 3 1 -> 5 2 1 -> 5 2 -> 5 B
5
2 3 4 5 1 -> 2 3 4 5 A
5
1 3 4 5 2 -> 1 3 4 5 A
5
5 4 1 2 3 -> 5 4 1 2 -> 5 4 1 -> 5 4 -> 5 B
5
10 7 9 2 5 8 4 1 3 6 -> 7 9 2 5 8 4 1 3 6 -> 9 2 5 8 4 1 3 6 -> 2 5 8 4 1 3 6 -> 5 8 4 1 3 6 -> 8 4 1 3 6 P
"""

