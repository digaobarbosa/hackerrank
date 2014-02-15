__author__ = 'digao'
__url__ = 'https://www.hackerrank.com/challenges/median'

import sys,StringIO
from bisect import *

def binary_search(arr,x):
    lo =0
    hi = len(arr)
    while lo<hi:
        mid = (lo+hi)/2
        if arr[mid]<x: lo = mid+1
        else: hi = mid
    return lo

def index(a, x,precise=True):
    'Locate the leftmost value exactly equal to x'
    i = binary_search(a, x)
    #same thing, but with bisect
    #i = bisect(a,x)

    if i != len(a) and ( a[i] == x or precise==False):
        return i
    return None


def operation(op,n,stack):
    if op=='r':
        i = index(stack,n)
        if i is not None:
            stack.pop(i)
            return stack
        return None
    elif op=='a':
        insort_left(stack,n)
        return stack


def main(input):
    f = True
    stack = []
    for line in input.readlines():
        if f:
            f = False
            continue
        op,n = line.strip().split()
        r = operation(op,int(n),stack)
        if r is None or not stack:
            print 'Wrong!'
        elif len(stack)%2==1:
            print stack[(len(stack)-1)/2]
        else:
            r=(stack[len(stack)/2]+stack[len(stack)/2-1])
            if r%2==1:
                r= r/2.0
            else:
                r = r/2
            print r










teste = """7
r 1
a 1
a 2
a 1
r 1
r 2
r 1
"""
main(StringIO.StringIO(teste))
#main2(StringIO.StringIO(teste))
#main(sys.stdin)