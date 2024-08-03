import pygame
import random

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, game):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.game = game
        self.image = pygame.image.load("Comet Fall Game/assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in pygame.sprite.spritecollide(self, self.game.all_monsters, False, pygame.sprite.collide_mask):
            monster.damage(self.player.attack)
            self.remove()
            if monster.health <= 0:
                monster.rect.x = 1000 + random.randint(0, 300)
                monster.velocity = random.randint(1, 3)
                monster.health = monster.max_health
            break

        if self.rect.x > 1080:
            self.remove()
