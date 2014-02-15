__author__ = 'digao'
__url__='https://www.hackerrank.com/challenges/two-arrays'
import sys,StringIO

def solve(A,B,K):
    A.sort()
    B.sort(reverse=True)
    for i in xrange(len(A)):
        a = A[i]
        b = B[i]
        if a+b < K:
            print 'NO'
            return
    print 'YES'


def main(input):
    T = int(input.readline())
    for t in xrange(T):
        N,K = map(int,input.readline().split())
        A = map(int,input.readline().split())
        B = map(int,input.readline().split())
        solve(A,B,K)



teste = """2
3 10
2 1 3
7 8 9
4 5
1 2 2 1
3 3 3 4
"""

main(StringIO.StringIO(teste))
#main(sys.stdin)
