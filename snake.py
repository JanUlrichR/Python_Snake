import pygame 

import constants


class Snake():
    
    def __init__(self,xpos,ypos):
        self.head_x = xpos
        self.head_y = ypos

        self.velocity = (0, 1)
        self.body = [(self.head_x-self.velocity[0],
                        self.head_y-self.velocity[1])]

    def update(self,fieldWidth,fieldHeight):
        new_headx =  self.head_x + self.velocity[0]
        new_heady = self.head_y + self.velocity[1]

        if new_headx < 0:
             new_headx = fieldWidth-1
        if new_headx >= fieldWidth:
            new_headx = 0 
        if new_heady < 0:
             new_heady = fieldHeight-1
        if new_heady >= fieldHeight:
            new_heady = 0 

        for i in range(len(self.body)):
            if new_headx == self.body[i][0] and new_heady == self.body[i][1]:
                return False 
        
        for i in reversed(range(len(self.body))):
            if i > 0:
                self.body[i] = self.body[i-1]
            else:
                self.body[i] = (self.head_x,self.head_y)
                
        self.head_x = new_headx
        self.head_y = new_heady

        return True

    def render(self,win):
        pygame.draw.rect(win,constants.SNAKE_HEAD_COLOR,(self.head_x * constants.FIELD_SIZE + constants.SNAKE_TO_FIELD_DIFF,
                                                    self.head_y * constants.FIELD_SIZE + constants.SNAKE_TO_FIELD_DIFF,
                                                    constants.SNAKE_SIZE,
                                                    constants.SNAKE_SIZE
                                                    ))

        for bodyPart in self.body :
            pygame.draw.rect(win,constants.SNAKE_COLOR,(bodyPart[0] * constants.FIELD_SIZE + constants.SNAKE_TO_FIELD_DIFF,
                                                    bodyPart[1] * constants.FIELD_SIZE + constants.SNAKE_TO_FIELD_DIFF,
                                                    constants.SNAKE_SIZE,
                                                    constants.SNAKE_SIZE
                                                    ))

    def getOccupiedCoords(self):
        return [(self.head_x,self.head_y)] + self.body 

    def grow(self):
        self.body.append((-5,-5))