#!usr/bin/python

'''
* * * Problem 16 * * *
*
* __author__ = 'j4ramos'
* __date__   = '3/13/2015'
*
* 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
*
* What is the sum of the digits of the number 2^1000?
'''

number = 2**1000

number_str = str(number)

the_sum = 0

for digit in number_str:
    the_sum += int(digit)

print the_sum
