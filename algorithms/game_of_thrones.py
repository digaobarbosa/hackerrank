
__url__="https://www.hackerrank.com/challenges/game-of-thrones"
__author__ = 'digao'
from StringIO import StringIO
import sys
import collections


def solve(line):
    letters = collections.defaultdict(lambda : 0)
    for c in line:
        letters[c] += 1
    l = len(line)
    if l%2==0:
        impares = [a for a in letters.values() if a%2 != 0]
        print impares and 'NO' or 'YES'
    else:
        impares = [a for a in letters.values() if a%2 != 0 ]
        print len(impares)!=1 and 'NO' or 'YES'



def main(input):
    for line in input.readlines():
            solve(line.strip())

test_input = """aaabbbb
cdefghmnopqrstuvw
"""

main(StringIO(test_input))
#main(sys.stdin)


