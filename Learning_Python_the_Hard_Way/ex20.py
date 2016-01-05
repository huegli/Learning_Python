# import argv from system package
from sys import argv

# input file as a command line argument
script, input_file = argv

# print the entire content of the file
def print_all(f):
    print f.read()
    
# go back to the beginning of the file
def rewind(f):
    f.seek(0)
    
# print only one line of the file
def print_a_line(line_count, f):
    print line_count, f.readline()
    
# open the file
current_file = open(input_file)

# and print it all
print "First let's print the whole file:\n"

print_all(current_file)
 
 # go back to begining
print "Now let's rewind, kind of like a tape."

rewind(current_file)

# print one line at a time
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
