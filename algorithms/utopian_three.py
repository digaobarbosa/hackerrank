__author__ = 'digao'
from StringIO import StringIO
import sys

cache = [1]

def solve(cycles):
    sum = 1
    if len(cache) > cycles+1:
        return cache[cycles]
    start = len(cache)
    sum = cache[-1]
    for i in range(start,cycles+1):
        if i%2==0:
            sum+=1
        else:
            sum = sum*2
        cache.append(sum)
    return sum

def main(input):
    N=None
    for line in input.readlines():
        if N is None:
            N = int(line.strip())
        else:
            print solve(int(line.strip()))

test_input = """5
0
1
2
3
4
5
6
"""

main(StringIO(test_input))
#main(sys.stdin)