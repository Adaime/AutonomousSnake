import pygame
from constants import GAME,SNAKE,APPLE,COLOR,SCALE


class Board:
	def __init__(self,display):
		self.board = [[0]*(GAME['ROW']) for i in range(GAME['COL'])]
		self.display = display
	
	def resetBoard(self):
		self.board = [[0]*(GAME['ROW']) for i in range(GAME['COL'])]


	def drawBoard(self,display,snake,apple):
		self.resetBoard() #newboard
		for body in snake: #add snake positions
			self.board[body[1]][body[0]] = 1 
		self.board[apple[1]][apple[0]] = -1 #add apple position

		self.display.fill(COLOR['BLACK']) # make screen black

	def returnBoard(self):
		return self.board # return board

	
