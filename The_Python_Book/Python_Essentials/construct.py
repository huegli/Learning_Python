#!/usr/bin/env python2

# We're going to write a program that will ask the user to input an arbitrary
# number of integers, store them in a collection, and then demonstrate how the
# collection would be used with various control structures

import sys # Used for the sys.exit function

target_int = raw_input("How many integers? ")

# By now, the variable target_int contains a string representation of 
# whatever the user typed. We need to try and convert that to an integer but
# be ready to deal with the error if it's not. Otherwise the program will
# crash.
try:
    target_int=int(target_int)
except ValueError:
    sys.exit("You must enter an integer")


ints = list()

count = 0

# Keep asking for an integer until we have the required number
while count < target_int:
    new_int = raw_input("Please enter integer {0}:" . format(count+1))
    isint=False
    try:
        new_int=int(new_int)
        isint=True
    except:
        print("You must enter an integer")


    # Only carry on if we have an integer. If not, we'll loop again
    # Notice below I use ==, which is different frmo =. The single equals is an
    # assignment operation whereas the double equals is a comparison operator.
    
    if isint==True:
        # Add the integer to the collection
        ints.append(new_int)
        # Increment the count by 1
        count += 1

print("Using a for loop")
for value in ints:
    print(str(value))

# Or with a while loop:
print("Using a while loop")
# We already have the total above, but knowin the len function is very 
# useful
total = len(ints)
count = 0
while count < total:
    print(str(ints[count]))
    count += 1
