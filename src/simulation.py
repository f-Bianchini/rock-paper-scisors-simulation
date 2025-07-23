import pygame
import numpy as np
import random
import Entity

def createEntities(rocks, papers, scissors):
    entities = []
    for i in range(rocks):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        velX = 25
        velY = 25
        entitiesVel = (velX if direction1 == 0 else velX * -1, 
                       velY if direction2 == 0 else velY * -1)
        entity = Entity.Entity("./assets/rock.png", "rock", (random.randint(50,250), random.randint(50,200)), entitiesVel)
        entities.append(entity)
    for i in range(papers):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        velX = random.randint(0,50)
        velY = random.randint(0,50)
        entitiesVel = (velX if direction1 == 0 else velX * -1, 
                       velY if direction2 == 0 else velY * -1)
        entity = Entity.Entity("./assets/paper.png", "paper", (random.randint(300,500), random.randint(250,400)), entitiesVel)
        entities.append(entity)
    for i in range(scissors):
        direction1 = random.randint(0,1)
        direction2 = random.randint(0,1)
        velX = random.randint(0,50)
        velY = random.randint(0,50)
        entitiesVel = (velX if direction1 == 0 else velX * -1, 
                       velY if direction2 == 0 else velY * -1)
        entity = Entity.Entity("./assets/scissors.png", "scissors", (random.randint(550,750), random.randint(450,575)), entitiesVel)
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

def CountTypes(entities: list[Entity.Entity]):
    rocks = 0
    papers = 0
    scissors = 0
    for i in range (len(entities)):
        if entities[i].type == "rock":
            rocks += 1
        elif entities[i].type == "paper":
            papers += 1
        elif entities[i].type == "scissors":
            scissors += 1
    return (rocks, papers, scissors)

pygame.init()
screen_height = 600
screen_width = 850
hud_height = 40
simulation_height = screen_height - hud_height
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
entities = createEntities(20, 20, 20)
font = pygame.font.SysFont(None, 36)
counters = (0,0,0)
running = True

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (0, hud_height, screen_width, simulation_height))
    pygame.draw.line(screen, (255, 255, 255), (0, hud_height), (screen_width, hud_height), 2)
    for entity in entities:
        entity.Update(dt, screen, hud_height)
    CheckEntitiesCollision(entities)
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, screen_width, hud_height))
    counters = CountTypes(entities)
    text = font.render(f"Rocks: {counters[0]} Papers: {counters[1]} Scissors: {counters[2]}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip() 
pygame.quit()