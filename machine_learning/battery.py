__author__ = 'digao'
__url__="https://www.hackerrank.com/challenges/battery"

import sys
from StringIO import StringIO

f = open('trainingdata.txt')
training = [line.strip() for line in f.readlines()]
training = map(lambda a:map(float,a.split(',')),training)
training.sort()
def main(input):
    data = float(input.readline())
    i=0
    for i in xrange(len(training)):
        t = training[i][0]
        if t==data:
            print training[i][1]
            return
        if t>data and i>0:
            dev = (training[i][1] - training[i-1][1])/(training[i][0] - training[i-1][0])
            time = training[i-1][1] + dev*(data - training[i-1][0])
            print time
            return

    print training[-1][1]


main(sys.stdin)