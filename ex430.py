# -*- coding: utf-8 -*-

from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("Arrival")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Delay(Scene):
    quips = [
        "Your flight is delayed.",
        "I think you will have to live here forever.",
        "HAHA you will never be comfortable again."
    ]
    def enter(self):
        print Delay.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Airport(Scene):
    def enter(self):
        print "Oh how exciting, you are going home for the Christmas Holidays"
        print "That sounds just like a lovely time, it is too bad you are so far away"
        print "If you want to have a nice holiday, you will first need to arrive,"
        print "you need to get on the airplane before it leaves "
        print "and do not forget your luggage"
        print "\n"
        print "You are rushing out of your taxi to get to the check in desk when"
        print "a group of grade school kids line up for their field trip."
        print "They are all standing in front of the check in desk blocking you."
        print "They are about to check in one after one when a new desk opens."
        print "They are fast, small, agile, and ahead of you...you (run, wait, fight)"

        action = raw_input("> ")

        if action == "run":
            print "Fast thinking!"
            print "Who told you it was a good idea to run through small children?"
            print "Don't you know that you could injure one of them, or worse, yourself."
            print "they are shuffeling around now"
            print "you weave in and out of them and toppel over one of their hello kitty backpacks"
            print "you suffer a concussion and have to go to the hospital. missin your flight. oops. "
            return 'Delay'

        elif action == "wait":
            print "Use your Buddhist training"
            print "take a deep breath"
            print "In"
            print "out"
            print "in"
            print "out"
            print "you wait forever."
            return 'Delay'

        elif action == "fight":
            print "you drop your suitcase"
            print "allowing both of your hands to be free "
            print "you reach in your pockets"
            print "find your smart phone and play a video"
            print "all the kids are distracted and subdued"
            print "you actually do not need to fight at all, just pick up your luggage and walk calmly to the desk"
            return 'going_through_security'

        else:
            print "DOES NOT COMPUTE!"
            return 'Airport'

class going_through_security(Scene):
    def enter(self):
        print "Boarding pass in hand"
        print "time to get on the plane"
        print "just another obstacle in the way, this time not as small as children"
        print "Hopefully you know your flight number"
        print "you have to tell the agent what it is to get through"
        print "wrong 3 times and you won't get through"
        print "get it right, otherwise you will not make it"
        #code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        code = ("069")
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "I am sorry, that flight doesn't exist, are you sure?!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        if guess == code:
            print "Thank you"
            print "You better hurry, your flight is leaving soon"
            print "please find your terminal"
            return 'Terminal'
        else:
            print "It is 2017, what kind of world are you living in"
            print "that you think you can get on a plane without your flight number"
            print "Ridiculous. You will freeze to death in this airport by the time you rememeber"
            return 'Delay'

class Terminal(Scene):
    def enter(self):
        print "You managed to get through security relatively unharmed"
        print "Ecxept for that body search, but you are fine"
        print "You have to make it though the terminal before check in is over"
        print "you run through the long hallways looking for your gate"
        print "you finally find it and you greet the ticket agent"
        print "She would like to see your documents."
        print "You serach through your bag"
        print "Your passport, boarding pass, are there"
        print "You have to give them to her in the right order do you give her them as:"
        print "first option: 1.passport 2.boarding pass"
        print "or"
        print "second option: 1.boarding pass 2.passport"

        action = raw_input("> ")

        if action == "first option":
            print "Hurridly you make the quick decision in your head"
            print "that of course she wants your passport first"
            print "a.nd you would be wrong"
            print "She does not accept your documents"
            print "and you have to sit inside the airport"
            print "watching the plane take off"
            return 'Delay'

        elif action == "second option":
            print "You take a risk giving her your boarding pass first"
            print "Would she even accept it not knowing who you are??"
            print "She cracks you a smile and you feel like maybe it is working"
            print "she takes your passports and compares the content"
            print "she scans both"
            print "you wait...and wait....and wait...for the red laser to beep"
            print "it finally does. you can board."
            print "you board the airplane"
            return 'Airplane'

        else:
            print "DOES NOT COMPUTE!"
            return "Terminal"

class Airplane(Scene):
    def enter(self):
        print "You go through the long tunnel"
        print "waiting behind the heard of people who also want to see their families"
        print "you enter the aircraft, seach for your seat"
        print "the ink on your boarding pass is smudged from your sweat"
        print "you need to decide which of the five free seats is yours"
        print "you have to take a risk"
        print "which one do you take?"
        #good_pod = randint(1,5)
        right_seat = 1
        guess = raw_input("[seat #]> ")

        if int(guess) != right_seat:
            print "OH OH OH! %s is not yours" % guess
            print "That is definitely the wrong seat..."
            print "The flight attendant comes and throws you off the plane for "
            print "disorderly conduct. "
            return 'Delay'
        else:
            print "Nervous you wait for everyone else to board the plane, "
            print " as you sit in seat %s" % guess
            print "You can see the last passengers board"
            print "none of them are coming for your seat"
            print "you sight a deep sigh of relief, finally you can breath"
            print "Now you can focus on seeing your family."
            return 'Arrival'


class Arrival(Scene):
    def enter(self):
        print "You fly 12 hours home without any more stress"
        print "Your family waits at your gate to pick you up."
        print "After 3 years, you can finally celebrate Christmas"
        print "With your family again. Merry Christmas."
        return 'Finished'


class Map(object):
    scenes = {
    'Airport': Airport(),
    'going_through_security': going_through_security(),
    'Terminal': Terminal(),
    'Airplane': Airplane(),
    'delay': Delay(),
    'Arrival': Arrival(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

#a_map = Map("Airport")
#a_game = Engine(a_map)
#a_game.play()
