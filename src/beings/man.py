import os
import pygame

class Man:
    def __init__(self, fpos=None):
        self.fpos = fpos if fpos is not None else (420.0, 420.0)
        self.image = pygame.image.load(
            os.path.join("assets", "man", "man.png")
        )

    @property
    def pos(self):
        x, y = self.fpos
        return (int(x), int(y))

    def blit(self, dest):
        dest.blit(self.image, self.pos)
