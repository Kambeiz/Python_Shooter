import pygame as pyg
from numba import jit, cuda

import animation
from game import Game

pyg.init()
@jit
def run():

    # def a clock
    clock = pyg.time.Clock()
    FPS = 60

    # Window generation
    pyg.display.set_caption("Comet Fall Game")
    screen = pyg.display.set_mode((1920,720))
    surface = screen.get_size()
    #surface = pyg.display.get_surface().get_size()
    # Background
    background = pyg.image.load("PygameAssets-main/bg.jpg")
    # banner for starting game
    banner = pyg.image.load('PygameAssets-main/banner.png')
    banner = pyg.transform.scale(banner, (500,500))
    banner_rect = banner.get_rect()
    banner_rect.x = 2*surface[0]/5
    banner_rect.y = 1*surface[1]/10
    # banner of game over
    gm_over = pyg.image.load("PygameAssets-main/game-over.png")
    gm = gm_over.get_rect()
    gm.x = 2*surface[0]/5
    gm.y = surface[1]/10

    # import button to play 
    play_button = pyg.image.load("PygameAssets-main/button.png")
    play_button =pyg.transform.scale(play_button, (300,100))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = banner_rect.x + 100
    play_button_rect.y = banner_rect.y + 425
    #loading the game
    game = Game()

    running = True

# A while checking the game running or not finished 
    while running:
        # Apply the background and maintaining the background:
        screen.blit(background,(0, -(surface[1] * 0.42)))
        
        
        # check if the game started (orn not)
        if game.is_playing == True:
            game.update(screen)
        else:
            if game.is_over == False:
                screen.blit(banner, (banner_rect.x, banner_rect.y)) 
                screen.blit(play_button, (play_button_rect.x,play_button_rect.y))
            elif game.is_over == True:
                screen.blit(gm_over, (gm.x, gm.y))
                screen.blit(play_button,(play_button_rect.x,play_button_rect.y))

        # update screen
        pyg.display.flip()

        for event in pyg.event.get():
        # Check if event is closed : 
            if event.type == pyg.QUIT:
                running = False
                pyg.quit()
                break
                print("Game have been left")
        
            # Detect if keyboard touched 
            elif event.type == pyg.KEYDOWN:
                # check which one 
                game.pressed[event.key] = True
                if event.key == pyg.K_SPACE:
                    if game.is_playing == True:
                    #print("right move")
                        game.player.launch_missile("right")
                    else:
                        game.sound_manager.play("click")
                        game.start() 
                elif event.key == pyg.K_w:
                    game.player.launch_missile("left")
                #elif event.key == pyg.K_LEFT:
                    #print("left move")
                #    game.player.move("left")
            # if no key is pressed : 
            elif event.type == pyg.KEYUP:
                game.pressed[event.key] = False
            
            elif event.type == pyg.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    # launch the game
                    game.sound_manager.play("click")
                    game.start() 
        
        # associating fps to clock
        clock.tick(FPS)

run()