# import argv from sys library
from sys import argv

# this will read the script name and an extra argument as the filename
script, filename = argv

# open the file with the filename given
txt = open(filename)

# this will read ithe content of the file and print it
print "Here is your file %r:" % filename
print txt.read()

#and close all files
txt.close()

