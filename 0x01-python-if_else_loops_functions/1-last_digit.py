#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    lastDigit = number % 10
else:
    lastDigit = ((number * -1) % 10) * -1

if lastDigit > 5:
    output = 'and is greater than 5'
elif lastDigit == 0:
    output = 'and is 0'
elif lastDigit < 6 and lastDigit != 0:
    output = 'and is less than 6 and not 0'

print(f'Last digit of {number} is {lastDigit} {output}')
