import pygame
import numpy as np
import random
import Entity

def createEntities(rocks, papers, scissors, entitiesVelocity):
    entities = []
    for i in range(rocks):
        entity = Entity.Entity("./assets/rock.png", (random.randint(0,100), random.randint(0,100)), entitiesVelocity)
        entities.append(entity)
    for i in range(papers):
        entity = Entity.Entity("./assets/paper.png", (random.randint(300,500), random.randint(300,500)), entitiesVelocity)
        entities.append(entity)
    for i in range(scissors):
        entity = Entity.Entity("./assets/scissors.png", (random.randint(500,700), random.randint(500,700)), entitiesVelocity)
        entities.append(entity)
    return entities

pygame.init()
screen = pygame.display.set_mode((960, 700))
clock = pygame.time.Clock()
entitiesVelocity = (10,10)
entities = createEntities(20, 20, 20, entitiesVelocity)
running = True
dt = 0

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for entity in entities:
        entity.Update(dt)
        entity.Draw(screen)
    pygame.display.flip()
pygame.quit()