import pygame as pyg
from comet import Comet
import random

# Class creation for manage the event 

class CometFallEvent:

    # Counter creation during loading of the event
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 20

        # sprite group definition for the comets
        self.all_comets = pyg.sprite.Group()

        # call game
        self.game = game

        # fall mode that will disable monsters

        self.fall_mode = False

    def meteor_fall(self):
        
        # choosing the nb of meteors
        meteor_nb = random.randint(10, 15)
        for i in range(0, meteor_nb):
           # loading one meteor
            self.all_comets.add(Comet(self))


    def add_percent(self, value=1):
        self.percent += self.percent_speed / 100
    
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0

    def attempt_fall(self):
        # if event bar full 
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Comet Fall !!")
            self.meteor_fall()
            #self.reset_percent()
            self.fall_mode = True

    def update_bar(self, surface):
        # add percent
        if self.percent >= 100:
            pass
        else:
            self.add_percent()
        
        # check event fall or not:
        #self.attempt_fall()

        # black background bar
        pyg.draw.rect(surface, (5, 5, 5), [25, surface.get_height() - 34, (surface.get_width() - 100), 20])

        # red bar, with the percent value and a slight change on the bar to be inside the black
        pyg.draw.rect(surface, (160, 0, 0), [30, surface.get_height() - 32, ((surface.get_width() - 106)/100)*self.percent, 16])
