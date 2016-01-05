def my_function(arg1, arg2):
    print "you called me"
    print "I see two arguments: %r and %r" % (arg1, arg2)
    print "Have a nice day"

print "First call:"
my_function(1,2)
print "Second call:"
my_function("Hello","World")
print "Third call:"
a=1; b=2
my_function(a,b)
print "Fourth call:"
my_function("Hello",a+b)