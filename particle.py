import pygame

class Particle(pygame.sprite.Sprite):

    def __init__(self, size):
        super().__init__()
        self.x = 0
        self.y = 0

        self.color = (255,255,255)
    
        self.image = pygame.Surface([size, size])
        pygame.draw.circle(self.image, self.color, (size / 2, size / 2), size / 2)
        self.rect = self.image.get_rect()

        self.directions = []
        occ = 100
        for i in range(0, occ):
            self.directions.append(i * (360 / occ))
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.center = self.x, self.y = pygame.mouse.get_pos()