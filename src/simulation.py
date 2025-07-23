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
        entity = Entity.Entity("./assets/paper.png", "paper", (random.randint(300,350), random.randint(250,350)), entitiesVel)
        entities.append(entity)
    for i in range(scissors):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        velX = random.randint(0,50)
        velY = random.randint(0,50)
        entitiesVel = (velX if direction1 == 0 else velX * -1, 
                       velY if direction2 == 0 else velY * -1)
        entity = Entity.Entity("./assets/scissors.png", "scissors", (random.randint(600,725), random.randint(400,525)), entitiesVel)
        entities.append(entity)
    return entities

def CheckEntitiesCollision(entities):
    for i in range(len(entities)):
        for j in range(len(entities)):
            if entities[i].CheckEntityCollision(entities[j]):
                CheckTypes(entities[i], entities[j])

def CheckTypes(first: Entity, second: Entity):
    if first.type == "rock" and second.type == "scissors":
        second.UpdateType(first.type, first.image)
    elif first.type == "paper" and second.type == "rock":
        second.UpdateType(first.type, first.image)
    elif first.type == "scissors" and second.type == "paper":
        second.UpdateType(first.type, first.image)

pygame.init()
screen = pygame.display.set_mode((750, 550))
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