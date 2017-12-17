from sys import exit
#Riding the Train
def differnt_seat():
    print "Congratulations on finding a new place to sit..."
    print "you found a lottery ticket"
    print "What was the winning number?"

    choice = raw_input ("> ")
    if "06" in choice or "18" in choice:
        lottery_win = int(choice)
    else:
        noSeat ("Too bad for you.")

    if lottery_win == 061:
        print "Good for you! This game costs 5 million to play, pay when you're finished."
        exit(0)
    else:
        noSeat("Whoops, better luck next time.")

#choice number 1:
def empty_window():
    print "You got the empty window seat."
    print "You put your bag above the seat, and take your phone from your pocket."
    print "You're phone is dead, your powerbank is in your bag."
    print "What do you do? \nGet your powerbank and lose your seat (get it), \n or small talk with your neighbor (small talk), \n put your headphones in and pretend that you're listening to music? (fake it)"
#Not sure what this does...
    empty_window = False

    while True:
        choice = raw_input ("> ")

        if choice == "get it":
            noSeat ("You stood up and lost your seat.")
        elif choice == "small talk" and not empty_window:
                print "Your neighbor forgot to brush his teeth, but you survived."
                empty_window = True
                noSeat("Way to go")
        elif choice == "fake it" and empty_window:
                noSeat("Nice quick problem solving ability")
        elif choice == "but your seat partner left and the stinky man sits next to you." and empty_window:
                stinky_man()
        else:
            print "you suffer, your train is delayed, and you have to stay on it forever."
            noSeat("bye!")


def stinky_man():
    print "OHHHH man, this is THE WORST"
    print "You're seat partner went jogging this morning TO the train station, so he hasn't showered."
    print "Do you hold your breath for the rest of the ride (hold breath) or do you tell him he needs a bath? (be rude)"

    choice = raw_input("< ")

    if choice == "hold breath":
        noSeat("That was a dumb mistake")
    elif choice == "be rude":
        noSeat("That was rude. He beat you up. ")
    else:
        print "you suffer, your train is delayed, and you have to stay on it forever, but you found a different seat."
        differnt_seat()

def noSeat(dundundun):
    print dundundun, "See you at your funeral"
    exit (0)

def start():
    print "You have to go to Tech Basics II in Hamburg."
    print "The train leaves soon, you have to get on."
    print "Which seat will you take? (1,2,3)"

    choice = raw_input("> ")

    if choice == "1":
        #bear_moved
        empty_window()
    elif choice == "2":
        #C room
        stinky_man()
    else:
        #dead
        noSeat("OHHHHH someone beat you there. Now you have to stand near the doors! Oh, and your mobile phone is dead. HA. HA. ")



start()
