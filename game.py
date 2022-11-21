import pygame as pyg
import animation
import sounds
from player import Player
from comet_event import CometFallEvent
from monster import *


# Game class

class Game():
    def __init__(self):
        # variable if game started or not
        self.is_playing = False
        # generate the player and the group
        self.all_players = pyg.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # sprites group monsters
        self.all_monsters = pyg.sprite.Group()
        self.pressed = {}
        self.spawn_monster(Monster_1)
        self.spawn_monster(Monster_2)
        self.is_over = False
        # generate comet event
        self.comet_event = CometFallEvent(self)
        #self.spawn_monster()
        self.font_score = pyg.font.Font("PygameAssets-main/Mulish-VariableFont_wght.ttf", 30)
        # Sound Manager
        self.sound_manager = sounds.SoundManager()
        self.score = 0
    def spawn_monster(self, monster_class_name):

        #monster = Monster_1
        self.all_monsters.add(monster_class_name.__call__(self))


    def start(self):
        self.is_playing = True
        self.spawn_monster(Monster_1)

    def game_over(self):
        self.all_monsters = pyg.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.is_over = True
        self.comet_event.reset_percent()
        self.comet_event.all_comets = pyg.sprite.Group()
        self.score = 0
        self.sound_manager.play("game_over")

    def add_score(self, points = 10):
        self.score += points

    def update(self, screen):

        # display score
        score_text = self.font_score.render(f"Score : {self.score}", 1, (255,255,255))
        screen.blit(score_text, (30, 30))

        # Add the player 
        screen.blit(self.player.image,self.player.rect)
        
        # Add the health bar of player
        self.player.update_health_bar(screen)

        # Event bar refresh
        self.comet_event.update_bar(screen)

        # Refresh player animation
        self.player.update_animation()

        # launching the movement of missiles and monster, before they are drawn 

        for missile in self.player.all_missiles:
            missile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
        
        # Recuperate comets 
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Draw the group of missiles
        self.player.all_missiles.draw(screen)
        
        # Add the monster group : 
        self.all_monsters.draw(screen)

        # Draw the meteor comet group
        self.comet_event.all_comets.draw(screen)


        #print(game.pressed)
        pyg.display.flip()
        
        # checking if the player want to go right/left
        if self.pressed.get(pyg.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move("right")
        elif self.pressed.get(pyg.K_LEFT) and self.player.rect.x > 0:
            self.player.move("left")
    
        
    def check_collision(self, sprite, group_sprites):
        return pyg.sprite.spritecollide(sprite, group_sprites, False, pyg.sprite.collide_mask)