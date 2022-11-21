import pygame as pyg
from missile import Missile
import animation

pyg.init
#s = pyg.display.get_surface()

# Create a class player

class Player(animation.AnimateSprite): #Heriting of the class of pygame sprite)
    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 4
        self.all_missiles = pyg.sprite.Group() 
        #self.animation = False
        self.miss_dir = ""
        #self.flipped = False
        #self.all_players = game.all_players
        #self.image = pyg.image.load("PygameAssets-main/player.png")
        self.rect = self.image.get_rect() # Take the image under a rectangle to move it
        #self.rect.x = 100
        #self.rect.y = 400
        s = pyg.display.get_surface()
        # taking a fixed position in the screeen according its height and width
        self.rect.x = s.get_width() * 0.50
        self.rect.y = s.get_height() * 0.56
    
    def update_health_bar(self,surface):

        # drawing the bar and its background
        pyg.draw.rect(surface, (60, 60, 60), [self.rect.x  + 50 , self.rect.y + 8, self.max_health + 4, 12])
        pyg.draw.rect(surface, (54,255,120), [self.rect.x + 52 , self.rect.y + 10, self.health, 8])

    def update_animation(self):
        if self.animation:
            if self.current_image <= 24 and self.miss_dir == "right":
                self.animate_1()
            elif self.current_image <= 24 and self.miss_dir == "left":
                self.animate_2()
            #self.animate_1(static = True)
        

    def move(self, direction):
        if direction =="left":
            self.rect.x -= self.velocity
        #elif not self.game.check_collision(self, self.game.all_monsters):
        elif direction == "right":
            self.rect.x += self.velocity

    def damage(self, amount):
        # Inflict damage
        if self.health >= 0:
            self.health -= amount
        else:
            #self.health == 0
            self.game.game_over()

    def launch_missile(self, direction):
        # init a new object of missile
        #missile = Missile()
        self.miss_dir = direction
        self.all_missiles.add(Missile(self,direction))
        # stopping animation here
        self.start_animation()
        self.game.sound_manager.play("tir")