import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, filepath, type, position, velocity):
        super().__init__()
        self.image = pygame.image.load(filepath).convert_alpha()
        self.type = type
        self.rect = self.image.get_rect(topleft=position)
        self.velocity = pygame.math.Vector2(velocity)
        self.pos = pygame.math.Vector2(position)

    def Update(self, dt):
        self.pos += self.velocity * dt
        self.rect.topleft = self.pos

    def Draw(self, screen):
        screen.blit(self.image, self.rect)
