__author__ = 'digao'
__url__ = 'https://www.hackerrank.com/challenges/median'

import sys,StringIO

def operation(op,n,stack):
    if op=='r':
        for i in xrange(len(stack)):
            e = stack[i]
            if e==n:
                stack.pop(i)
                return stack
            elif e>n:
                return None
    elif op=='a':
        for i in xrange(len(stack)):
            e = stack[i]
            if e>n:
                stack.insert(i,n)
                return stack
        stack.append(n)
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
            print (stack[len(stack)/2]+stack[len(stack)/2-1])/2.0










teste = """7
r 1
a 1
a 2
a 1
r 1
r 2
r 1"""
main(StringIO.StringIO(teste))
#main2(StringIO.StringIO(teste))
#main(sys.stdin)