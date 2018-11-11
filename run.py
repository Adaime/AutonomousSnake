from apple import Apple
from board import Board
from snake import Snake
from algorthim import DFS
import pygame
from constants import GAME,SNAKE,APPLE,COLOR,SCALE 
import time
import random
from a import *



#GAMELOOP
class Game:

    def __init__(self, display):
        self.display = display #instance
        self.score = 0
    
    def loop(self):
        #TIME
        clock = pygame.time.Clock()


        #INSTANCE
        board = Board(self.display)
        apple = Apple(self.display)
        snake = Snake(self.display)

        #ACTUAL GAMELOOP
        while True:
            path = astar(board.returnBoard(), snake.snake_pos(),apple.apple_Position())
            print(path)
            for i in range(1,len(path)):

                #if next move is not orthogonal
                if snake.changeDirectionTo(snake.CoordinateToDirection(path[i])): 
                    path = astar(board.returnBoard(), snake.snake_pos(),apple.apple_Position())
                    

                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("exit pressed!")
                        return 0




                # DRAW BACKGROUND
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake.changeDirectionTo('UP')    
                    elif event.key == pygame.K_DOWN:
                        snake.changeDirectionTo('DOWN')              
                    elif event.key == pygame.K_LEFT:
                        snake.changeDirectionTo('LEFT')                 
                    elif event.key == pygame.K_RIGHT:
                        snake.changeDirectionTo('RIGHT')

                # MOVE SNAKE and record position of SNAKE
                snake.move()




                # Collision Detection
                if snake.collision():
                    return 0

                #eating
                if snake.ate(apple.apple_Position()):
                    self.score += 1
                    pygame.display.set_caption(GAME['CAPTION']+ str(self.score))
                    apple.randomize()


                #DRAW
                board.drawBoard(self.display,snake.snake_body(),apple.apple_Position())
                apple.draw()
                snake.draw_body()

                
                #DRAW UPDATE
                pygame.display.update()
                clock.tick(GAME['FPS'])

def main():
    display = pygame.display.set_mode((GAME['WIDTH'],GAME['HEIGHT']))
    pygame.display.set_caption(GAME['CAPTION'])
    
    game = Game(display)
    value = game.loop()
    
    #LINUX EXIT COMMANDS
    if value != 0:
        print("Game ended wrong: ", value)
        exit(1)

if __name__ == '__main__':
	main()
