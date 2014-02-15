__author__ = 'digao'
__url__ = "https://www.hackerrank.com/challenges/quicksort1"

import sys,StringIO

def partition(arr,comp):
    smaller = []
    bigger = []
    for e in arr:
        if e <=comp:
            smaller.append(e)
        else:
            bigger.append(e)
    return (smaller,bigger)

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    s,b = partition(arr[1:],pivot)
    arr = quick_sort(s)+[pivot]+quick_sort(b)
    print ' '.join(map(str,arr))
    return arr


def main(input):
    N = int(input.readline())
    arr = map(int,input.readline().split())
    quick_sort(arr)



teste = """3
5 8 1 3 7 9 2
"""

main(StringIO.StringIO(teste))
#main(sys.stdin)
