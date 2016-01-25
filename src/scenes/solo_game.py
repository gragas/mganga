import sys

import pygame
import requests

from buffalo import utils
from buffalo.button import Button
from buffalo.label import Label
from buffalo.option import Option
from buffalo.scene import Scene

class SoloGame(Scene):
    def __init__(self, server, ip, port):
        Scene.__init__(self)
        self.server = server
        self.ip = ip
        self.port = port

    def blit(self):
        pass

    def stop(self):
        if hasattr(self, "server"):
            requests.post("http://{}:{}/shutdown".format(self.ip, self.port))
            self.server.terminate()
            self.server.join()        

    def on_escape(self):
        self.stop()
        sys.exit(0)
