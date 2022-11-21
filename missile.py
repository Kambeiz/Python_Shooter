import pygame as pyg

# Managing the player missile

class Missile(pyg.sprite.Sprite):

    # init the constructor
    def __init__(self, player, direction):
        super().__init__()
        self.player = player
        self.velocity = 2
        self.image = pyg.image.load('PygameAssets-main/projectile.png')
        self.image = pyg.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 4* player.image.get_size()[0]/9
        self.rect.y = player.rect.y + player.image.get_size()[1]/2
        self.origin_image = self.image
        self.angle = 0
        self.direction = direction 
    def move(self):
        if self.direction == "right":
            self.rect.x += self.velocity 
            self.rotate()
        elif self.direction == "left":
            self.rect.x -= self.velocity 
            self.rotate()
        if self.rect.x > pyg.display.get_surface().get_width() or self.rect.x < 0: 
            self.remove()
#        elif self.rect.x < 0:
#            self.remove()
        
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            monster.damage(self.player.attack)
            self.remove()
            

    def remove(self):
        self.player.all_missiles.remove(self)
        #print("deleted")

    def rotate(self):
        # rotating the missile
        self.angle += 8
        self.image = pyg.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)