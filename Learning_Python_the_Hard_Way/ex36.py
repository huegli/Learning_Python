from sys import exit

actions = 0

def pub_room():
    global actions
    
    print "Ford tells you that the earth is about to be blown up."

    for i in range(actions+5, 0, -1):
        print "%d ..." % i

    print "=== THE END ==="
    print "Roll credits...."
    exit(0)

def bath_room():
    global actions
    print "You walk into the bathroom, the blinds are shut."

    while not vogons_here_yet():

        choice = raw_input("> ")

        if "open blinds" in choice:
            print "You see a tractor about to crush your house."

            choice = raw_input("> ")
            if "run outside" in choice:
                outside_room()
            else:
                dead("The tractor crushes your house with you in it.")
        else:
           print "You do exactly that."
           actions += 1
        
    dead("")


def outside_room():
    global actions
    
    print "You run outside and lie in front of the tractor."
    print "Ford Prefect comes by and asks if you are busy."

    while not vogons_here_yet():
        choice = raw_input("> ")

        if "yes" in choice:
            dead("'Too bad', he says and disapears. Shortly afterwards, the Vogons blow up the earth.")
        elif "no" in choice:
            print "'Great', he says and you both go to a pub"
            pub_room()
        else:
            print "'Sorry, I don't understand', says Ford"
            actions += 1
    dead("")


def vogons_here_yet():
    global actions

    if (actions < 5):
        return False
    else:
        return True

def dead(why):

    if (len(why) == 0):
        why = "The earth gets blown up by the Vogon construction fleet."

    print why, "Good job!"
    exit(0)

def start():
    global actions

    print "You wake up with a hangover."

    while not vogons_here_yet():

        choice = raw_input("> ")

        if "bathroom" in choice:
            bath_room()
        else:
            print "I don't understand what you mean."
            actions += 1

    dead("")

start()
