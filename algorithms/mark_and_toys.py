__author__ = 'digao'
__url__ = 'https://www.hackerrank.com/challenges/mark-and-toys'

import sys,StringIO

def solve(prices,K):
    prices.sort()
    s = 0
    count = 0
    for p in prices:
        if s+p <= K:
            s+=p
            count+=1
        else:
            return count
    return count

def main(input):
    N,K = map(int,input.readline().strip().split())
    prices = map(int,input.readline().strip().split())
    print solve(prices,K)


teste = """7 50
1 12 5 111 200 1000 10"""

main(StringIO.StringIO(teste))
#main(sys.stdin)