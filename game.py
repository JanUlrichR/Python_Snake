import pygame

from snake import Snake
from apple import Apple
import constants

class Game:

    def __init__(self):
        pass

    def init(self,winWidth,winHeight):
        self.fieldWidth = winWidth // constants.FIELD_SIZE
        self.fieldHeight = winHeight // constants.FIELD_SIZE 

        
        self.snake = Snake(self.fieldWidth // 2, self.fieldHeight //2)
        self.apple = Apple(self.snake.getOccupiedCoords(), self.fieldWidth, self.fieldHeight)
        self.currentTick = 0
        self.score = 0

    def update(self):
        res = True
        self.currentTick += 1
        if self.currentTick > 5:
            res = res and self.snake.update(self.fieldWidth,self.fieldHeight)
            snakeBlocks =  self.snake.getOccupiedCoords()
            if self.apple.pos in snakeBlocks:
                self.snake.grow()
                self.apple = Apple(snakeBlocks,self.fieldWidth,self.fieldHeight)

            self.currentTick = 0
        
        if res == False:
            #Death
            print("[GAMEOVER] Snakelength : "+ str(len(self.snake.body)+1))

        return res

    def render(self,win):
        #First render the field
        #To make the lines shorter
        fz = constants.FIELD_SIZE
        for y in range(self.fieldHeight):
            for x in range(self.fieldWidth):
                pygame.draw.rect(win,constants.FIELD_COLOR,(x*fz,y*fz,fz,fz),constants.FIELD_BORDER_SIZE)

        self.snake.render(win)

        self.apple.render(win)

