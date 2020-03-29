#env = Basics
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


import pygame
from game import Game

import constants

#Declare variables
game = Game()

#On create method
def onCreate():
    game.init(constants.WIN_WIDTH,constants.WIN_HEIGHT)

#update method
def update():
    return game.update()

#render method
def render(win):
    win.fill(constants.BACKGROUND_COLOR)

    game.render(win)
    
    pygame.display.update()

def onKeydown(keys):
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        game.snake.velocity = (0,-1)

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        game.snake.velocity = (0,1)

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        game.snake.velocity = (1,0)

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        game.snake.velocity = (-1,0)















































# No Need to change this 


if __name__ == "__main__":
    pygame.init()

    win = pygame.display.set_mode((constants.WIN_HEIGHT,constants.WIN_WIDTH))
    pygame.display.set_caption("Snake")

    running = True

    #OnCreate call
    onCreate()

    while(running):
        pygame.time.delay(constants.GAME_DELAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        #OnKeyDown
        onKeydown(keys)
        
        #update / render call

        running = running and update()
        render(win)




