import pygame
import numpy as np
import random
import Entity

def createEntities(rocks, papers, scissors, entitiesVelocity):
    entities = []
    for i in range(rocks):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        entitiesVel = (entitiesVelocity if direction1 == 0 else entitiesVelocity * -1, 
                       entitiesVelocity if direction2 == 0 else entitiesVelocity * -1)
        entity = Entity.Entity("./assets/rock.png", "rock", (random.randint(0,100), random.randint(0,100)), entitiesVel)
        entities.append(entity)
    for i in range(papers):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        entitiesVel = (entitiesVelocity if direction1 == 0 else entitiesVelocity * -1, 
                       entitiesVelocity if direction2 == 0 else entitiesVelocity * -1)
        entity = Entity.Entity("./assets/paper.png", "paper", (random.randint(300,500), random.randint(300,500)), entitiesVel)
        entities.append(entity)
    for i in range(scissors):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        entitiesVel = (entitiesVelocity if direction1 == 0 else entitiesVelocity * -1, 
                       entitiesVelocity if direction2 == 0 else entitiesVelocity * -1)
        entity = Entity.Entity("./assets/scissors.png", "scissors", (random.randint(500,700), random.randint(500,700)), entitiesVel)
        entities.append(entity)
    return entities

pygame.init()
screen = pygame.display.set_mode((960, 700))
clock = pygame.time.Clock()
entitiesVelocity = 20
entities = createEntities(20, 20, 20, entitiesVelocity)
running = True

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for entity in entities:
        entity.Update(dt)
        entity.Draw(screen)
    pygame.display.flip()
pygame.quit()