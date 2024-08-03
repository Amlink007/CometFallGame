import pygame


class SoundManager:
    
    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("Comet Fall Game/assets/sounds/click.ogg"),
            "game_over": pygame.mixer.Sound("Comet Fall Game/assets/sounds/game_over.ogg"),
            "meteorite": pygame.mixer.Sound("Comet Fall Game/assets/sounds/meteorite.ogg"),
            "tir": pygame.mixer.Sound("Comet Fall Game/assets/sounds/tir.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()
