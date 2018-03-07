#!/usr/bin/python
from __future__ import print_function

# This program says hello and asks for my name.

print('Hello World!')
print('What is your name?')	# ask for their name
myName = input()
print('It is good to meet you, {}'.format(myName))
print('The length of your name is:')
print(len(myName))
print('What is your age?')	# ask for their age
myAge = input()
print('You will be {} in a year.'.format(str(int(myAge) + 1)))
