__author__ = 'digao'
from StringIO import StringIO
import sys,re

def add_it(numbers,n):
    for i in xrange(len(numbers)):
        k = numbers[i]
        if k>n:
            return numbers[:i]+[n]+numbers[i:]
    numbers.append(n)
    return numbers

def del_it(numbers,n):
        numbers.remove(n)
        return numbers


def median(numbers):
    n = len(numbers)
    if n==0:
        return 'Wrong!'
    if n%2==0:
        return (numbers[n/2]+numbers[n/2-1])/2.
    return numbers[n/2]


def solve(numbers,op,n):
    if 'r'==op:
        try:
            numbers = del_it(numbers,n)
        except ValueError:
            print 'Wrong!'
            return numbers
    elif 'a'==op:
        numbers = add_it(numbers,n)
    print median(numbers)
    return numbers




def main(input):
    N=None
    numbers = []
    for line in input.readlines():
        if N is None:
            N = True
        else:
            op,n = line.strip().split()
            numbers = solve(numbers,op,int(n))


test_input = """7
r 1
a 1
a 2
a 1
r 1
r 2
r 1"""

main(StringIO(test_input))
#main(sys.stdin)