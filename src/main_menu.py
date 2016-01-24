import pygame

from buffalo import utils
from buffalo.label import Label
from buffalo.scene import Scene

class MainMenu(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.labels.add(
            Label(
                (5, 5),
                "Mganga Version 0.0.1",
            )
        )

    def blit(self):
        pass

    def on_escape(self):
        exit(0)
