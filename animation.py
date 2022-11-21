import pygame as pyg
import random

# Class creation for animation
class AnimateSprite(pyg.sprite.Sprite):

    # def the init for animate
    def __init__(self, sprite_name, size=(200,200)):
        super().__init__()
        self.sprite_name = sprite_name
        self.orig_image = pyg.image.load(f"PygameAssets-main/{sprite_name}.png")
        self.image = self.orig_image
        self.image = pyg.transform.scale(self.image, size)
        self.current_image = 0
        self.flipped = False
        self.animation = False
        self.size = size
        
    # def stuff for animate
        self.frames = animation_dict(sprite_name)

    def animate_1(self, animation = True):
        if animation == True:
            # next frame
            self.current_image += 1

            # limit of 24
            # if self.current_image >= 24:
            if self.current_image >= len(self.frames):
                # reset
                self.current_image = 0
                self.animation = False
            #self.flipped = flipping_overiding

            # changing the frame itself
            #self.is_flipping()
            #print(self.flipped)
            self.image = self.frames[self.current_image]
            self.image = pyg.transform.scale(self.image, self.size)
    def animate_2(self):
        # next frame
        self.current_image += 1

        # limit of 24
        # if self.current_image >= 24:
        if self.current_image >= len(self.frames):
            # reset
            self.current_image = 0
            self.animation = False

        #self.flipped = flipping_overiding

        # changing the frame itself
        #self.is_flipping()
        #print(self.flipped)
        self.image = self.frames[self.current_image]
 
        self.image = pyg.transform.flip(self.image,True, False)
        self.image = pyg.transform.scale(self.image, self.size)


    def start_animation(self):
        self.animation = True

    def get_sprite_name(self):
       return self.sprite_name

#    def is_flipping(self, next_frame):
#        if self.flipped == False:
#                next_frame = pyg.transform.flip(next_frame,True, False)
#                #elf.flipped = True
#                return next_frame
#        elif self.flipped:
#                next_frame = pyg.transform.flip(next_frame,False, False)
#                return next_frame
#        else:
#            return next_frame

def load_animation_images(sprite_name):
    # loading frames
    frames = []

    # getting path of folder for the sprite
    path = f"PygameAssets-main/{sprite_name}/{sprite_name}"

    # looping frame, knowing their number
    for num in range(1, 25): 
        frame = path + str(num) + '.png' # another way to do it is to import a module os, or glob, to iterate over the folder and recuperate their names
        img = pyg.image.load(frame)
        frames.append(img)
    return frames

# dict definition containing each frame of each sprite
def animation_dict(sprite_name = "mummy"):
    animation = {}
    animation[sprite_name] =  load_animation_images(sprite_name)
    return load_animation_images(sprite_name)