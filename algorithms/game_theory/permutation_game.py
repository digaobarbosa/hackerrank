__author__ = 'digao'
from StringIO import StringIO
import sys

def inv(i):
    return i=='Alice' and 'Bob' or 'Alice'
way =[]
def solve(numbers):
    for i in xrange(len(numbers)):
        if solve_p(numbers,i,'Alice')=='Alice':
            return 'Alice'
    return 'Bob'

def is_won(numbers):
    last=0
    for i in numbers:
        if i < last:
            return False
        last = i
    return True

cache = {}

def solve_p(numbers,p,person):
    new_sequence = numbers[:p]+numbers[(p+1):]
    key = ','.join(map(str,new_sequence))
    if key in cache: return cache[key] and person or inv(person)
    if is_won(new_sequence):
        cache[key] = True
        return person
    else:
        #jogada do outro
        other = inv(person)
        for i in xrange(len(new_sequence)):
            r = solve_p(new_sequence,i,other)
            if r == other:
                cache[key] = False
                return other
        cache[key] = True
        return person







    #key = ','.join(numbers)

def test():
    print solve(map(int,'10 7 9 2 5 8 4 1 3 6'.split()))=='Bob'
    print solve(map(int,'6 4 1 5 3 2'.split()))=='Alice'
    print solve(map(int,'1 3 2 4 5'.split()))=='Alice'
    print solve(map(int,'6 3 5 4 1 2'.split()))=='Alice'
    print solve(map(int,'8 1 6 9 2 3 4 5 7'.split()))=='Alice'
    print solve(map(int,'4 3 2 6 1 5'.split()))=='Alice'
    print solve(map(int,'11 9 10 5 8 3 2 7 6 4 1'.split()))=='Alice'
    print solve(map(int,'10 7 9 2 5 8 4 1 3 6'.split()))=='Alice'
    print solve(map(int,'3 4 5 1 2'.split()))=='Bob'
    print solve(map(int,'15 2 4 10 12 13 8 7 11 14 1 6 5 9 3'.split()))=='Alice'
    print solve(map(int,'9 4 7 10 13 12 8 6 2 5 1 14 3 15 11'.split()))=='Alice'

def main(input):
    N=None
    count = 0
    for line in input.readlines():
        if N is None:
            N = int(line.strip())
        else:
            if count%2==1:
               print solve(map(int,line.strip().split()))
            count+=1

test_input = """2
3
1 3 2
5
5 3 2 1 4
5
5 2 3 4 1
5
2 3 4 5 1
5
1 3 4 5 2
5
5 4 1 2 3
"""


main(sys.stdin)
#test()
#print '------------------'
#main(StringIO(test_input))


a_test_input = """2
3
1 3 2 -> 1 2 A
5
5 3 2 1 4 -> 3 2 1 4 -> 3 2 1 -> 2 1 -> 1 B
5
5 2 3 4 1 -> 5 2 3 1 -> 5 2 1 -> 5 2 -> 5 B
5
2 3 4 5 1 -> 2 3 4 5 A
5
1 3 4 5 2 -> 1 3 4 5 A
5
5 4 1 2 3 -> 5 4 1 2 -> 5 4 1 -> 5 4 -> 5 B
5
10 7 9 2 5 8 4 1 3 6 -> 7 9 2 5 8 4 1 3 6 -> 9 2 5 8 4 1 3 6 -> 2 5 8 4 1 3 6 -> 5 8 4 1 3 6 -> 8 4 1 3 6 P
"""

