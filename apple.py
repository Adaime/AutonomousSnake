from constants import GAME,SNAKE,APPLE,COLOR,SCALE
import random
import pygame

class Apple:
    def __init__(self,display):
        self.display = display
        self.x_pos = random.randint(GAME['ORIGIN'],GAME['ROW']-1)#-1 is to stay within range of game
        self.y_pos = random.randint(GAME['ORIGIN'],GAME['COL']-1)
        # self.snake_body = snake_body

    def draw(self):
        return pygame.draw.rect(
            self.display,
            COLOR['WHITE'],
            [   
                self.positionToPixel()[0],
                self.positionToPixel()[1],
                (GAME['WIDTH']/GAME['ROW']),
                (GAME['HEIGHT']/GAME['COL'])               
            ])
    def positionToPixel(self):
        return [self.x_pos*(GAME['WIDTH']/GAME['ROW']),self.y_pos*(GAME['HEIGHT']/GAME['COL'])]

    def apple_Position(self):
        return (self.x_pos,self.y_pos)

    def randomize(self):
        self.x_pos = random.randint(GAME['ORIGIN'],GAME['ROW']-1)
        self.y_pos = random.randint(GAME['ORIGIN'],GAME['COL']-1)
        # while ([self.x_pos,self.y_pos] in snake_body):
        #         self.x_pos = round(random.randint(GAME['ORIGIN'],GAME['WIDTH']-GAME['BLOCK'])/GAME['BLOCK'])*GAME['BLOCK']
        #         self.y_pos = round(random.randint(GAME['ORIGIN'],GAME['HEIGHT']-GAME['BLOCK'])/GAME['BLOCK'])*GAME['BLOCK']

    def updateBoard(self):
        self.board[self.x_pos][self.y_pos] = 1


    

