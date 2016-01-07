print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

def vogon_fleet():
    print "You are teleported to the Vogon construction fleet."
    print "The crew discovers you and brings you to the captain."
    print "1. Do you want to be thrown out of the air lock?"
    print "2. Do you want to listen to some poetry?"
        
    poetry = raw_input("> ")
    
    if poetry == "1":
        print "You are picked up by the Heart of Gold 59 seconds later. Good job!"
    elif poetry == "2":
        print "You die a slow and horrible death listening to Vogon poetry. Good job!"
    else:
        print "You get teleported to stone age earth. Good job!"
   
door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Call the Vogon Construction fleet."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        vogon_fleet()
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yello jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    print "4. 42."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    elif insanity == "4":
        print "You found the answer to life, the universe and everything. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
        
       
else:
    print "You stumble around and fall on a knife and die.  Good job!"