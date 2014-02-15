__author__ = 'digao'
__url__ = "https://www.hackerrank.com/challenges/quicksort1"

import sys,StringIO

def partition(arr):
    comp = arr[0]
    smaller = []
    bigger = []
    for e in arr[1:]:
        if e <=comp:
            smaller.append(e)
        else:
            bigger.append(e)
    return smaller+[comp]+bigger

def main(input):
    N = int(input.readline())
    arr = map(int,input.readline().split())
    print ' '.join(map(str,partition(arr)))



teste = """3
4 5 3 7 2
"""

main(StringIO.StringIO(teste))
#main(sys.stdin)
