#!usr/bin/python

'''
* * * Problem 13 * * *
* __author__ = 'j4ramos'
* __date__   = '3/13/2015'
* 
* Work out the first ten digits of the sum of 
* the following one-hundred 50-digit numbers.
*
'''

with open('problem13_numbers.txt', 'r') as f:

    text = f.readlines()
    numbers = [int(line) for line in text]

the_sum = 0

for number in numbers:
    the_sum += number

sum_str = str(the_sum)

print sum_str[:10]
