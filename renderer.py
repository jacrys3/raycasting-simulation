from fileinput import close
from platform import python_branch
from random import randrange
import pygame
from pygame.locals import *
from particle import Particle
from line import Line
import math
 
class Renderer:

    def __init__(self):
        self.running = True
        self.surface = None
        self.size = self.width, self.height = 640, 400
        self.dot = None
        self.walls = []
 
    def on_init(self):
        pygame.init()
        self.surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
        self.dot = Particle(15)
        self.create_walls()
        
    def create_walls(self):
        for i in range(0, 5):
            line = Line((randrange(0, self.width), randrange(0, self.height)), (randrange(0, self.width), randrange(0, self.height)), self.surface)
            self.walls.append(line)

        self.walls.append(Line((0, 0), (self.width, 0), self.surface))
        self.walls.append(Line((0, 0), (0, self.height), self.surface))
        self.walls.append(Line((self.width, self.height), (0, self.height), self.surface))
        self.walls.append(Line((self.width, self.height), (self.width, 0), self.surface))\
        

    def draw_walls(self):
        for line in self.walls:
            line.draw()

    def draw_rays(self):
        for dir in self.dot.directions:
            closest = ()
            record = float("inf")
            for wall in self.walls:
                point = self.cast(dir, wall)
                if(point):
                    x, y = point
                    distance = (abs((x - self.dot.x) + abs((y - self.dot.y))))
                    if(distance < record):
                        record = distance
                        closest = point
            if(closest):
                x, y = closest
                pygame.draw.line(self.surface, (255, 255, 255), (self.dot.x, self.dot.y), (int(x), int(y)))

    def cast(self, direction, wall):
        x1 = wall.x1
        y1 = wall.y1
        x2 = wall.x2
        y2 = wall.y2

        x3 = self.dot.x
        y3 = self.dot.y
        x4 = self.dot.x - math.cos(math.radians(direction))
        y4 = self.dot.y - math.sin(math.radians(direction))

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if t > 0 and t < 1 and u > 0:
            point = ((x1 + t * (x2 - x1)), (y1 + t * (y2 - y1)))
            return point
        else:
            return None

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_render(self):
        new_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.surface.blit(new_surface, (0, 0))

        self.dot.draw(self.surface)
        self.dot.update()
        self.draw_walls()
        self.draw_rays()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False
 
        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    window = Renderer()
    window.on_execute()