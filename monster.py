import pygame as pyg
import random
import animation

#from main import surface 
# Create Monster Class

class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0): 
    #def __init__(self, game):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.velocity = 2
        #self.flipped = False
        self.count_death = 0
        self.animation = True
        self.origin_image = self.image
        self.rect = self.image.get_rect()
        #self.rect.x = screen.get_size()[0] - 50
        self.ini_x = pyg.display.get_surface().get_size()[0] - 100
        self.ini_y = pyg.display.get_surface().get_size()[1] * 0.62
        self.rect.x = self.ini_x
        self.rect.y = self.ini_y - offset

    def update_health_bar(self,surface):
        # drawing the bar and its background
        pyg.draw.rect(surface, (60, 60, 60), [self.rect.x + 13, self.rect.y - 22, self.max_health + 4, 12])
        pyg.draw.rect(surface, (48,87,247), [self.rect.x + 15, self.rect.y - 20, self.health, 8])

    def damage(self, amount):
        # Inflict damage
        self.health -= amount

    def update_animation(self):
        if self.velocity > 0:
            self.flipped = True
            self.animate_1()
        elif self.velocity < 0 :
            self.flipped == False
            self.animate_2()

    def self_loot_amount(self, amount):
        self.loot_amount = amount

    def forward(self):
        # Collision 
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

class Monster_1(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130,130))
        #Monster.__init__(self,game)
        #animation.AnimateSprite.__init__(self,"mummy")
        #super(Monster).__init__("mummy")
        #self.image = pyg.image.load("PygameAssets-main/mummy.png")
        self.origin_image = self.image
        self.rect = self.image.get_rect()
        #self.rect.x = screen.get_size()[0] - 50
        self.ini_x = pyg.display.get_surface().get_size()[0] - 100
        self.ini_y = pyg.display.get_surface().get_size()[1] * 0.62
        self.rect.x = self.ini_x
        self.rect.y = self.ini_y
        self.self_loot_amount(20)

    def respawn(self):

        if self.health <= 0 :
            # killing it and respawn it  
            self.health = self.max_health
            #self.velocity = random.choice([-1*self.velocity, self.velocity])
            new_velo = list(range(-2,2))
            new_velo.remove(0)
            self.velocity = random.choice(new_velo)
            if self.velocity > 0:
                self.flipped = True
                #if self.flipped == True:
                    #self.is_flipping()
                    #print(self.flipped)
                    #self.flipped = False
                self.rect.x = self.ini_x

            elif self.velocity < 0 :
                self.flipped == False
                #self.flipped == False:
                    #print(self.flipped)
                    #self.is_flipping()
                    #self.flipped = True
                self.rect.x = pyg.display.get_surface().get_size()[0] / 9
            #self.rect.x = 100 + random.randint(-1, 1) * self.ini_x + random.randint(-100,500)
            self.rect.y = self.ini_y 
            self.count_death += 1
            self.game.add_score(20)

    def damage(self, amount):
        super().damage(amount)

        # if we have more than 10x 2 monsters proc
        if self.count_death >= 10 and self.health <= 0:
            #print(self.count_death)
            self.game.all_monsters.remove(self)
            return
        elif self.game.comet_event.is_full_loaded():
            if self.health <= 0 :
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()
        self.respawn()
        #self.update_animation()

class Monster_2(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 150)
        self.health = 250
        self.max_health = 250
        self.velocity = 4
        self.attack = 20
        self.self_loot_amount(50)

    def update_health_bar(self,surface):
        # drawing the bar and its background
        pyg.draw.rect(surface, (60, 60, 60), [self.rect.x + 20, self.rect.y - 22, self.max_health + 4, 16])
        pyg.draw.rect(surface, (48,87,247), [self.rect.x + 22, self.rect.y - 20, self.health, 12])



    def damage(self, amount):
        super().damage(amount)
        if self.health <= 0:
            #print(self.count_death)
            self.game.all_monsters.remove(self)
            self.game.add_score(self.loot_amount)
            return

        # if we have more than 10x 2 monsters proc
        if self.count_death >= 10 and self.health <= 0:
            #print(self.count_death)
            self.game.all_monsters.remove(self)
            return
        #self.respawn()
        #self.update_animation()
