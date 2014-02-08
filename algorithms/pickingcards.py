__author__ = 'digao'
__url__ = 'https://www.hackerrank.com/challenges/picking-cards'


from StringIO import StringIO
import sys



mod = 1000000007

def solve(N,cards):
    cards.sort()
    picked = 0
    combinations = 1
    index = 0
    while picked <N:
        while index < N-1 and cards[index+1] <= picked :
            index+=1
        combinations = (combinations*(index+1 - picked))%mod
        picked += 1
        if combinations==0: return combinations
    return combinations





def main(input):
    first = True
    CASES = int(input.readline())
    for i in xrange(CASES):
        n = int(input.readline().strip())
        cards = map(int,input.readline().strip().split())
        print solve(n, cards)


test_input = """3
3
0 0 1
3
0 3 3
3
0 0 0"""

main(StringIO(test_input))
#main(sys.stdin)






