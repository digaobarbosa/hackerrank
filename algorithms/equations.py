__author__ = 'digao'
__url__ = 'https://www.hackerrank.com/challenges/equations'


from StringIO import StringIO
import sys



def is_prime(n,primes):
    i=0
    k = primes[0]
    while k<=n/2 and i<len(primes):
        k = primes[i]
        if n%k==0: return False
        i+=1

    return True

mod = 1000007

def solve(N):
    primes = [2,3]
    for i in xrange(4,N+1):
        if is_prime(i,primes):
            primes.append(i)
    prime_factor = []
    for p in primes:
        n = N/p
        S = (n+1)*n/2
        prime_factor.append(S)

    return reduce(lambda a,x:a*(2*x+1),prime_factor,1)%mod






def main(input):
    for line in input.readlines():
            print solve(int(line.strip()))

test_input = """4
5
6
1
2
3
"""

main(StringIO(test_input))
#main(sys.stdin)






