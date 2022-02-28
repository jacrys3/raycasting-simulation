import pygame

class Line:
    
    def __init__(self, start, end, surface):
        self.start = self.x1, self.y1 = start
        self.end = self.x2, self.y2 = end
        self.surface = surface

        self.color = (255,255,255)
    
        pygame.draw.line(self.surface, self.color, start, end, 1)

    def draw(self):
        pygame.draw.line(self.surface, self.color, self.start, self.end, 1)

