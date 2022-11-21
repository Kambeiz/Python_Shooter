import pygame as pyg
import monster
import random

# CLass for the comet itself

class Comet(pyg.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()

        # loading the comet sprite  
        self.image = pyg.image.load("PygameAssets-main/comet.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, pyg.display.get_surface().get_size()[0])
        self.rect.y = -random.randint(0, pyg.display.get_surface().get_size()[1])
        self.velocity = random.randint(1,3)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        
        # check if comet number = 0 to check if fall comet done
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent() # we reset the bar
            # spawn monsters again
            self.comet_event.game.spawn_monster(monster.Monster_1)
            self.comet_event.game.spawn_monster(monster.Monster_1)

    def fall(self):
        self.rect.y += self.velocity  
        # if it touch the ground
        if self.rect.y >= (pyg.display.get_surface().get_height() * 0.56):
            #print("sol")
            self.comet_event.game.sound_manager.play("meteorite")
            self.remove()
        elif self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.damage()
        # check number of comets

        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.fall_mode= False

    def damage(self):
        # check contact player meteor
        print("Contact meteor!!!")
        self.comet_event.game.sound_manager.play("meteorite")

        # remove the meteor after contact
        self.remove()
        # taking damage
        self.comet_event.game.player.damage(30)

