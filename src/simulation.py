import pygame
import numpy as np
import random
import Entity

def createEntities(rocks, papers, scissors):
    entities = []
    for i in range(rocks):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        velX = random.randint(0,50)
        velY = random.randint(0,50)
        entitiesVel = (velX if direction1 == 0 else velX * -1, 
                       velY if direction2 == 0 else velY * -1)
        entity = Entity.Entity("./assets/rock.png", "rock", (random.randint(50,100), random.randint(50,100)), entitiesVel)
        entities.append(entity)
    for i in range(papers):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        velX = random.randint(0,50)
        velY = random.randint(0,50)
        entitiesVel = (velX if direction1 == 0 else velX * -1, 
                       velY if direction2 == 0 else velY * -1)
        entity = Entity.Entity("./assets/paper.png", "paper", (random.randint(300,500), random.randint(300,500)), entitiesVel)
        entities.append(entity)
    for i in range(scissors):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        velX = random.randint(0,50)
        velY = random.randint(0,50)
        entitiesVel = (velX if direction1 == 0 else velX * -1, 
                       velY if direction2 == 0 else velY * -1)
        entity = Entity.Entity("./assets/scissors.png", "scissors", (random.randint(500,650), random.randint(500,650)), entitiesVel)
        entities.append(entity)
    return entities

def CheckEntitiesCollision(entities):
    for i in range(len(entities)):
        for j in range(len(entities) - (i+1)):
            if entities[i].CheckEntityCollision(entities[j]):
                entities[j].UpdateType(entities[i].type, entities[i].image)
pygame.init()
screen = pygame.display.set_mode((960, 700))
clock = pygame.time.Clock()
entities = createEntities(20, 20, 20)
running = True

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for entity in entities:
        entity.Update(dt, screen)
        CheckEntitiesCollision(entities)
    pygame.display.flip()
pygame.quit()