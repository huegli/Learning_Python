# import argv from system package
from sys import argv

script, filename = argv

# This is simply because we haven't learned if statement yet	
print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl-C (^C)"
print "If you want that, hit ENTER."

# read an input, Ctrl-C will quit
raw_input("?")

# open the file, for writing this time
print "Opening the file..."
target = open(filename, "w")


# this isn't really necessary
# print "Truncating the file. Goodbye!"
# otarget.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we are close."
target.close()



