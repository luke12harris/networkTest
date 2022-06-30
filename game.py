import pygame
pygame.init()

# set up the game window
screen = pygame.display.set_mode((420, 420)) #dimensions of screen
pygame.display.set_caption("Pac Man") # screen title

pacPng = pygame.image.load("pacman.png")
pacX = 0
pacY = 0
pacXChange = 0
pacYChange = 0
speed = 0.02

def Pac (x,y): # draws pacman, x,y are new co'ords
    screen.blit(pacPng, (x, y))

# run until the user asks to quit
running = True
while running:
    screen.fill("white")

    for event in pygame.event.get(): # event.get() outs a list of all events that occur
        if event.type == pygame.QUIT: # user press the X button
            running = False

        if event.type == pygame.KEYDOWN: # pressed key
            if event.key == pygame.K_LEFT:
                pacXChange = -speed
                pacYChange = 0

            if event.key == pygame.K_RIGHT:
                pacXChange = +speed
                pacYChange = 0

            if event.key == pygame.K_UP:
                pacXChange = 0
                pacYChange = -speed

            if event.key == pygame.K_DOWN:
                pacXChange = 0
                pacYChange = +speed

    #changes the co'ords of pacman
    pacX += pacXChange
    pacY += pacYChange


    Pac(pacX, pacY) # updates the position of pacman

    pygame.display.update()

pygame.quit()
