__author__ = 'digao'
from StringIO import StringIO
import sys,re

def solve(numbers):
    numbers.sort()
    min_diff = 10**9
    before = None
    diff_list = []
    for a in numbers:
        if before != None and abs(a-before)<min_diff:
            min_diff = abs(a-before)
            diff_list = [str(before),str(a)]
        elif before != None and abs(a-before)==min_diff:
            diff_list.append(str(before))
            diff_list.append(str(a))
        before = a
    return diff_list

def main(input):
    N=None
    for line in input.readlines():
        if N is None:
            N=True
        else:
            res = solve(map(int,line.strip().split()))
            print ' '.join(res)

test_input = """10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854"""

main(StringIO(test_input))
#main(sys.stdin)