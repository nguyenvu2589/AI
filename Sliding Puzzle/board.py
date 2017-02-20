import json
import numpy as np
import pprint
from read_file import *
from validatation import *
from rule import locate_zero
import scipy.spatial as spatial

class board:
	def __init__(self, board):
		self.goal = board['goal']
		self.board = board['start']
		self.n = board['n']
		self.path = []

	def print_board(self):
		print self.board 

	# find position of zero
	# p1.locate_zero()

	def is_goal(self): 
		return (self.board == self.goal)
			
	# when blank space make a move. call rule() function.
	# should create a swap function that can swap array. 
	# move pos only give the old and new pos . then swap
	# take care the rest.
	def moves(self,move):
		zero = locate_zero(self.board)
		row = zero[0][0]
		col = zero[0][1]
		if move == 'up':
			self.swap(row, col, row-1, col)
		if move == 'down':
			self.swap(row, col, row+1, col)
		if move == 'left':
			self.swap(row, col, row, col-1)
		if move == 'right':
			self.swap(row, col, row, col+1)

		return self.board

	# swap the board element postion.
	def swap(self,r1,c1,r2,c2):
		temp = self.board[r1][c1]
		self.board[r1][c1] = self.board[r2][c2]
		self.board[r2][c2] = temp

	# f(n) = g(n) + h(n)
	# g(n) : manhathan 
	# might be able to use from rules. 
	# try to call locate_zero.....
	

	def heuristic(self, id):
		current_pos = locate_id(self.board,id)
		goal_pos = locate_id(self.goal,id)
		return spatial.distance.cityblock(goal_pos, current_pos)

	def heuristic_sum(self):
		total = 0 
		for i in range (1, (self.n)**2 ):
			total = total + self.heuristic(i)
	
def locate_id(board, id):
		return zip(*np.where(np.array(board) == id))

def compare(old, new):
	return True if old.board == new.board else False

	# if old.board == new.board:
	# 	return True
	# else:
	# 	return False