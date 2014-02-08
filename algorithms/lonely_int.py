__author__ = 'digao'
from StringIO import StringIO
import sys


def solve(array):
    N = len(array)
    array.sort()
    before = None
    if N==1:
        return array[0]
    for a in array:
        if before != None and before==a:
            before=None
        elif before is None:
            before = a
        else:
            return before
    return before


def main(input):
    N = None
    for line in input.readlines():
        if N is None:
            N = True
        else:
            print solve(map(int, line.strip().split()))


test_input = """3
1 5 3 2 1 3 5
"""

main(StringIO(test_input))
#main(sys.stdin)