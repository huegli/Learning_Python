print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "And what is your first name? ",
first = raw_input("-> ")
last = raw_input("Last name? ")
print "Hello, %s!!!" % (first + " " + last)
