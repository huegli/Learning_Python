# import argv from sys library
from sys import argv

# this will read the script name and an extra argument as the filename
script, filename = argv

# open the file with the filename given
txt = open(filename)

# this will read ithe content of the file and print it
print "Here is your file %r:" % filename
print txt.read()

# enter new filename, this time with raw_input
print "Type the filename again:"
file_again = raw_input("> ")

# open the new file
txt_again = open(file_again)

# and read / print it
print txt_again.read()

#and close all files
txt.close()
txt_again.close()

