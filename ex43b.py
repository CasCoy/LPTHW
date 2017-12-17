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
        last_scene = self.scene_map.next_scene("arrived")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Delay(Scene):

    quips = [
        "Your flight will is delayed.",
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
            print "you actually do note need to fight at all, just pick up your luggage and walk calmly to the desk"
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
        print "wrong 10 times then the lock closes forever and you can’t"
        print "get the bomb. The code is 3 digits."
        #code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        code = ("123")
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven’t pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don’t want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can’t get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don’t have time to look. There’s 5 pods, which one"
        print "do you take?"
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!"
            return 'finished'


class Finished(Scene):
    def enter(self):
        print "You won! Good job."
        return 'finished'

class Map(object):
    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
