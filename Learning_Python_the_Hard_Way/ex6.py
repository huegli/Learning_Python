# string assignments
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print out strings
print x
print y

# literal printing of strings
print "I said: %r." % x
print "I also said: '%s'." % y

# use variables for both formatter and values
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# string concatenation 
w = "This is the left side of..."
e = "a string with a right side."

print w + e
