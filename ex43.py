#Game Concept: Flying Home for the Holidays
#Arrival; Winning the game and arriving safely at Home
#Train: starting point getting to the airport
#airport: trouble encountered at the encountered
#airplane: no food
# Airplane, Airport, Train, Terminal, Suitcases, Flight Attendant, Seat, Security, Scene, Passport,
# *itinerary *scenes: Train, Airport, Airplane, Security
    #ITINERARY: *opening_scene, *next_scene
    #SCENE: *enter , death, train, airport, airplane, Security
    #Engine -play
from sys import exist
from random import randit


class Scene(object):
    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
