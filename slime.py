import random
import math
import imageio
import numpy as np
import copy

WIDTH = int(500)
HEIGHT = int(500)

FRAMES = 50

images = []

agents = []

baseimage = np.zeros((WIDTH,HEIGHT),dtype=np.uint8)


class agent():

    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.angle = random.randrange(360)

    def collision(self):
        self.angle = 360 - self.angle + (random.randrange(9000)/100)

    def motor(self):
        radians = self.angle * math.pi / 180
        #add a multiple by velocity
        self.x = self.x + math.cos(radians)
        self.y = self.y + math.sin(radians)
        if not(0 < self.x < WIDTH):
            self.collision()

        if not(0 < self.y < HEIGHT):
            self.collision()


def movement():
    for a in agents:
        a.motor()

def render():
    for a in agents:
        baseimage[int(a.x),int(a.y)] = 255
    
    images.append(copy.deepcopy(baseimage))
    

for i in range(10):
    agents.append(agent())


for i in range(FRAMES):
    movement()
    render()

imageio.mimsave('test.gif',images)



    