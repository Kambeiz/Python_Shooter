import pygame as pyg

class SoundManager:

    def __init__(self):
        self.sounds = {"click": pyg.mixer.Sound("PygameAssets-main/sounds/click.ogg"),
        "game_over": pyg.mixer.Sound("PygameAssets-main/sounds/game_over.ogg"),
        "tir" : pyg.mixer.Sound("PygameAssets-main/sounds/tir.ogg"),
        "meteorite" : pyg.mixer.Sound("PygameAssets-main/sounds/meteorite.ogg") }


    def play(self,name):
        self.sounds[name].play()