from constants import GAME,SNAKE,APPLE,COLOR,SCALE
import pygame

#SNAKE
class Snake:
    def __init__(self,display):
        self.display = display
        self.x_pos = GAME['ORIGIN'] 
        self.y_pos = GAME['ORIGIN']
        self.direction = ''
        self.body = []
        self.current_size = 1
        self.path = []


    def changeDirectionTo(self,MOVE):
        if MOVE == 'RIGHT' and self.direction != "LEFT":
            self.direction = 'RIGHT'
        elif MOVE == 'LEFT' and self.direction != "RIGHT":
            self.direction = 'LEFT'
        elif MOVE == 'UP' and self.direction != "DOWN":
            self.direction = 'UP'
        elif MOVE == 'DOWN' and self.direction != "UP":
            self.direction = 'DOWN' 
    
    def CoordinateToDirection(self,nextmove):
        if self.y_pos == nextmove[1]:
            if self.x_pos == nextmove[0]+1:
                return "LEFT"
            elif self.x_pos == nextmove[0]-1:
                return "RIGHT"
        elif self.x_pos == nextmove[0]:
            if self.y_pos == nextmove[1]+1:
                return "UP"
            elif self.y_pos == nextmove[1]-1:
                return "DOWN"           

    def move(self):
        if self.direction == 'RIGHT' :
            self.x_pos += 1
        elif self.direction == 'LEFT' :
            self.x_pos -= 1
        elif self.direction == 'UP' :
            self.y_pos -= 1
        elif self.direction == 'DOWN':
            self.y_pos += 1

        self.body.append([self.x_pos,self.y_pos])
        if len(self.body) > self.current_size:
            del(self.body[0])
    def ate(self,food):
        if food[0] == self.x_pos and food[1] == self.y_pos:
            self.current_size += 1 
            return True
        return False

    def positionToPixel(self):
        return [self.x_pos*(GAME['WIDTH']/GAME['ROW']),self.y_pos*(GAME['HEIGHT']/GAME['COL'])]


    def draw_body(self):
        #return ends the function 

        for bodyPart in self.body:
            pygame.draw.rect(self.display,
            COLOR['WHITE'],
            [   
                bodyPart[0]*(GAME['WIDTH']/GAME['ROW']),
                bodyPart[1]*(GAME['HEIGHT']/GAME['COL']),
                (GAME['WIDTH']/GAME['ROW']),
                (GAME['HEIGHT']/GAME['COL'])                
            ]
            )

    def snake_body(self):
        return self.body

    def snake_pos(self):
        return (self.x_pos,self.y_pos)

    def checkcollision(self,move):
        if move in self.body:
            return True
        elif (move[0] *(GAME['WIDTH']/GAME['ROW']) < GAME['ORIGIN']) or (move[0] *(GAME['WIDTH']/GAME['ROW']) >= GAME['WIDTH']) or (move[1]*(GAME['HEIGHT']/GAME['COL']) < GAME['ORIGIN']) or (move[1]*(GAME['HEIGHT']/GAME['COL']) >= GAME['HEIGHT']):
            return True

        return False

    def avoidcollision(self):
        choices = []
        if not self.checkcollision(self.x_pos+1,self,y_pos):
            choices.append("RIGHT")
        if not self.checkcollision(self.x_pos-1,self,y_pos):
            choices.append("LEFT")
        if not self.checkcollision(self.x_pos,self,y_pos-1):
            choices.append("UP")
        if not self.checkcollision(self.x_pos+1,self,y_pos+1):
            choices.append("DOWN")

        return choices



    def collision(self):
        for body in self.body[:len(self.body)-1]:
            if body == [self.x_pos,self.y_pos]:
                print("snake ate itself")
                return True

        if (self.positionToPixel()[0] < GAME['ORIGIN']) or (self.positionToPixel()[0] >= GAME['WIDTH']) or (self.positionToPixel()[1] < GAME['ORIGIN']) or (self.positionToPixel()[1] >= GAME['HEIGHT']):
            print("snake hit a wall")
            return True 
        
        return False

   

