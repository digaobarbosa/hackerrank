__author__ = 'digao'
__url__="https://www.hackerrank.com/challenges/predicting-house-prices"
from StringIO import StringIO
import sys
__doc__= """
Thinking in matrices we have three: F (features),T(factors) and P (prices)
The main idea here is to find the values of T that minimizes the difference
between F*T-P
F*T = P

Thinking on 2 features as the example we have:

|1 0 |     10
|0 1 |      10
|2 1 |*T =  30
|1 0 |      15


So T is a 2x1 matrix. To minimize the difference we can see that for each line,
ideally we should have:


(1*t1 - 10)
(1*t2 -10)
(2*t1+1*t1 - 30)
(1*t1 -15)


To find such T, we think in matrix.

F'*F*T = F'P
T = inv(F'*F)*F'*P


Common least square optimization.

"""
import numpy





def main(input):
    F = None
    N = None
    table = []

    F, N = map(int, input.readline().strip().split())
    P = []
    for i in xrange(N):
        line = map(float,input.readline().strip().split())
        table.append(line[:-1])
        P.append([line[-1]])

    F = numpy.matrix(table)
    T = ((F.T*F).I*F.T)*numpy.matrix(P)
    cases = int(input.readline())
    for i in xrange(cases):
        fs = map(float,input.readline().strip().split())
        v = (fs*T)[0,0]
        print v









test="""2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18
"""

main(StringIO(test))
main(sys.stdin)



