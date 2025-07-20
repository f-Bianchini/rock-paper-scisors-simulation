import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, filepath, position, velocity=(0, 0)):
        super().__init__()
        self.image = pygame.image.load(filepath).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.velocity = pygame.math.Vector2(velocity)

    def Update(self, dt):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

    def Draw(self, surface):
        surface.blit(self.image, self.rect)
