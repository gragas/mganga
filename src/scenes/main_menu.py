from multiprocessing import Process
import sys

import pygame
import requests

from buffalo import utils
from buffalo.button import Button
from buffalo.label import Label
from buffalo.option import Option
from buffalo.scene import Scene

import server
from scenes.solo_game import SoloGame

class MainMenu(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.labels.add(
            Label(
                (5, 5),
                "Mganga Version 0.0.1",
            )
        )

        self.port = 5000
        self.local_server = True

        def new_world():
            self.server = Process(target=server.app.run, args=(self.ip,))
            self.server.start()
            utils.set_scene(SoloGame(self.server, self.ip, self.port))

        def stop():
            if hasattr(self, "server"):
                requests.post("http://{}:{}/shutdown".format(self.ip, self.port))
                self.server.terminate()
                self.server.join()

        def shutdown():
            stop()
            sys.exit(0)

        self.buttons.add(
            Button(
                utils.SCREEN_M,
                "New World",
                x_centered=True,
                y_centered=True,
                func=new_world,
            )
        )

        self.buttons.add(
            Button(
                (utils.SCREEN_W // 2, utils.SCREEN_H // 2 + 100),
                "Exit",
                x_centered=True,
                y_centered=True,
                func=shutdown,
            )
        )

    @property
    def ip(self):
        return "127.0.0.1" if self.local_server else "0.0.0.0"

    def blit(self):
        pass

    def on_escape(self):
        exit(0)
