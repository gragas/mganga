import os
import pygame

from buffalo import utils

class You:
    def __init__(self, fpos=None):

        def get_centered_pos():
            x, y = utils.SCREEN_M
            return (x - 16.0, y - 16.0)

        self.fpos = fpos if fpos is not None else get_centered_pos()
        self.image = pygame.image.load(
            os.path.join("assets", "man", "man.png")
        )
        self.speed = 0.025

    def update(self, keys):
        x, y = self.fpos
        xv, yv = 0.0, 0.0
        up, down, left, right = (
            keys[pygame.K_w],
            keys[pygame.K_s],
            keys[pygame.K_a],
            keys[pygame.K_d],
        )
        if right:
            xv = self.speed
        if left:
            xv = -self.speed
        if up:
            yv = -self.speed
        if down:
            yv = self.speed
        if (left or right) and (up or down):
            xv *= 0.7071
            yv *= 0.7071
        xv *= utils.delta
        yv *= utils.delta
        self.fpos = x + xv, y + yv

    @property
    def pos(self):
        x, y = self.fpos
        return (int(x), int(y))

    def blit(self, dest):
        dest.blit(self.image, self.pos)
