import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, filepath, type, position, velocity):
        super().__init__()
        self.image = pygame.image.load(filepath).convert_alpha()
        self.type = type
        self.rect = self.image.get_rect(topleft=position)
        self.velocity = pygame.math.Vector2(velocity)
        self.pos = pygame.math.Vector2(position)

    def Update(self, dt, screen):
        self.pos += self.velocity * dt
        self.rect.topleft = self.pos
        self.CheckBorderCollision(screen.get_height(), screen.get_width())
        self.Draw(screen)

    def Draw(self, screen):
        screen.blit(self.image, self.rect)

    def CheckBorderCollision(self, screenHeight, screenWidth):
        if self.pos.x <= 0 or self.pos.x + self.rect.width >= screenWidth:
            self.velocity.x *= -1
        if self.pos.y <= 0 or self.pos.y + self.rect.height >= screenHeight:
            self.velocity.y *= -1
    
    def CheckEntityCollision(self, other):
        if self.pos.distance_to(other.pos) <= 16:
            return True
        return False

    def UpdateType(self, newType, newImage):
        self.image = newImage
        self.type = newType
        print(self.type)