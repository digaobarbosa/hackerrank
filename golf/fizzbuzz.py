__author__ = 'digao'
__url__='https://www.hackerrank.com/challenges/fizzbuzz'

for i in range(1,101):print i%15==0 and 'FizzBuzz' or (i%5==0 and 'Buzz' or (i%3==0 and 'Fizz' or i))

for x in range(100):print 'Fizz'*(x%3/2)+'Buzz'*(x%5/4) or x+1



