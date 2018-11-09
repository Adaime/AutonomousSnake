import pygame
from constants import GAME,SNAKE,APPLE,COLOR 
from board import Board


class DFS():
	def __init__(self,board):
		self.board = board
		self.stack = [] #directions in coordinates
		self.visited = [] #everything visited
		self.path = [] #directions in names
		self.hamiltonCycle = []
		self.directions = []
	def newBoard(self,newBoard):
		self.board = newBoard

	def ai(self,snakehead,apple):
		position = snakehead
		target = apple
		path = self.hamiltonCycle()
		directions = self.changeToDirection(path)
		return directions
		# self.stack.append(snakehead)
		# self.visited.append(snakehead)

		# if the body is less than or equal to 4

			# while position != target:

			# 	if position[0] > target[0]:
			# 		position[0] -= 1
			# 		self.stack.append("LEFT")
				
			# 	elif position[0] < target[0]:
			# 		position[0] += 1
			# 		self.stack.append("RIGHT")

			# 	elif position[1] > target[1]:
			# 		position[1] -= 1
			# 		self.stack.append("UP")

			# 	elif position[1] < target[1]:
			# 		position[1] += 1
			# 		self.stack.append("DOWN") 

			# return self.stack

		# elif 
			#create a hamilton path (CALL FUNCTION) => have it return a path
			# in that path

		#get the body of the snake
		#find the head location of the snake in the path
		#find the 2nd last tail of the snake in the path
		# make a list of possible moves that can be conducted
		#  ^ process can be reiterated for each move,
		# if there is no direct path to the food, move around
		#
def hamiltonpath(self):
	for i in range(0,GAME['HEIGHT'],GAME['BLOCK']*2):
		for j in range(GAME['BLOCK'],GAME['WIDTH'],GAME['BLOCK']):
			self.hamiltonCycle.append([j,i])
		for k in range(GAME['WIDTH']-GAME['BLOCK'],GAME['ORIGIN'],-GAME['BLOCK']):
			self.hamiltonCycle.append([k,i+GAME['BLOCK']])

	for l in range(GAME['HEIGHT']-GAME['BLOCK'],-GAME['BLOCK'],-GAME['BLOCK']):
		self.hamiltonCycle.append([GAME['ORIGIN'],l])

	return self.hamiltonCycle

def changeToDirection(self,path):
	for i in range(len(path)):
		if path[i][1] == path[i-1][1]:
			if path[i][0] == path[i-1][0]+GAME['BLOCK']:
				self.directions.append("RIGHT")
			elif path[i][0] == path[i-1][0]-GAME['BLOCK']:
				self.directions.append("LEFT")
		elif self.hamiltonCycle[i][0] == path[i-1][0]:
			if path[i][1] == path[i-1][1]+GAME['BLOCK']:
				self.directions.append("DOWN")
			elif path[i][1] == path[i-1][1]-GAME['BLOCK']:
				self.directions.append("UP")

	return self.directions


  #       return self.hamiltonCycle
		# return self.stack
 

	# def ai(self,snakehead,apple):
	# 	position = snakehead
	# 	target = apple
	# 	self.stack.append(snakehead)
	# 	self.visited.append(snakehead)

	# 	while self.stack[-1] != target:
	# 		if self.posInBoard([self.stack[-1][0] - 1,self.stack[-1][1]]) and [self.stack[-1][0] - 1,self.stack[-1][1]] not in self.visited:
	# 			self.path.append('DOWN')
	# 			self.stack.append([self.stack[-1][0] - 1,self.stack[-1][1]])
	# 			self.visited.append([self.stack[-1][0] - 1,self.stack[-1][1]])
	# 		elif self.posInBoard([self.stack[-1][0] + 1,self.stack[-1][1]]) and [self.stack[-1][0] + 1,self.stack[-1][1]] not in self.visited:
	# 			self.path.append('UP')
	# 			self.stack.append([self.stack[-1][0] + 1,self.stack[-1][1]])
	# 			self.visited.append([self.stack[-1][0] + 1,self.stack[-1][1]])
	# 		elif self.posInBoard([self.stack[-1][0] - 1,self.stack[-1][1]]) and [self.stack[-1][0] ,self.stack[-1][1]- 1] not in self.visited:
	# 			self.path.append('LEFT')
	# 			self.stack.append([self.stack[-1][0],self.stack[-1][1] - 1 ])
	# 			self.visited.append([self.stack[-1][0] - 1,self.stack[-1][1] - 1 ])
	# 		elif self.posInBoard([self.stack[-1][0],self.stack[-1][1]]) and [self.stack[-1][0] ,self.stack[-1][1]+ 1] not in self.visited:
	# 			self.path.append('RIGHT')
	# 			self.stack.append([self.stack[-1][0],self.stack[-1][1] + 1 ])
	# 			self.visited.append([self.stack[-1][0],self.stack[-1][1] + 1 ])

	# 		else:
	# 			self.stack.remove(self.stack[-1])
	# 			self.path.remove(self.path[-1])

	# 	print("returns")
	# 	return self.path

	def posInBoard(self,position):
		pos = [position[0]*(GAME['WIDTH']/GAME['ROW']),position[1]*(GAME['HEIGHT']/GAME['COL'])]
		print(pos)
		if (pos[0] < GAME['ORIGIN']) or (pos[0] >= GAME['WIDTH']) or (pos[1] < GAME['ORIGIN']) or (pos[1] >= GAME['HEIGHT']):
			print("works")
			return False 

		return True

