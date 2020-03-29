import random
import constants
import pygame

class Apple():
    
    def __init__(self, occList, fieldWidth,fieldHeight):
        possfields = set()

        for poss_X in range(fieldWidth):
            for poss_Y in range(fieldWidth):
                possfields.add((poss_X,poss_Y))


        for occField in occList:
            possfields.discard(occField)

        self.pos = random.sample(possfields,1)[0]

    def render(self, win):
        pygame.draw.circle(win,constants.APPLE_COLOR,(int(self.pos[0]*50+constants.FIELD_SIZE/2),
                                                        int(self.pos[1]*50+constants.FIELD_SIZE/2)),
                                                        constants.APPLE_RADIUS)
