from __future__ import print_function

import random
import textwrap

if __name__ == '__main__':
    keep_playing = 'y'
    occupants = ['enemy', 'friend', 'unoccupied']
    width = 72
    dotted_line = '-' * width
    print(dotted_line)
    print("\033[1m" + "Attack of The Orcs v0.0.1:" + "\033[0m")

    msg = (
        "The war between humans and their arch enemies, Orcs was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he decided to enter...")

    print(textwrap.fill(msg, width=width))
    print("\033[1m" + "Mission:" + "\033[0m")
    print("\tChoose a hut where Sir Foo can rest...")
    print("\033[1m" + "TIP:" + "\033[0m")
    print("Be careful as there are enemies lurking around!")
    print(dotted_line)

    while keep_playing == 'y':
        huts = []
        # Randomly append 'enemy' or 'friend' or None to the husts list
        while len(huts) < 5:
            computer_choice = random.choice(occupants)
            huts.append(computer_choice)

        # Prompt user to select a hut
        msg = "\033[1m" + "Choose a hut number to enter (1-5):" + "\033[0m"
        user_choice = raw_input("\n" + msg)
        idx = int(user_choice)

        # Print the occupant info
        print("Revealing the occupants...")
        msg = ""
        for i in range(len(huts)):
            occupant_info = "<%d:%s>"%(i+1, huts[i])
            if i + 1 == idx:
                occupant_info = "\033[1m" + occupant_info + "\033[0m"
            msg += occupant_info + " "
        print("\t" + msg)
        print(dotted_line)
        print("\033[1m" + "Entering hut %d..." % idx + "\033[0m", end=' ')

        # Determine and announce the winner
        if huts[idx-1] == 'enemy':
            print("\033[1m" + "YOU LOSE :( Better luck next time!" +
                  "\033[0m")
        else:
            print("\033[1m" + "Congratulations! YOU WIN!!!" + "\033[0m")
        print(dotted_line)
        keep_playing = raw_input("Play again? Yes(y)/No(n):")
