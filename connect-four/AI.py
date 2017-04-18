from board import *
from check_status import *
from copy import deepcopy
import random

class AI(object):
	def __init__(self,object):
		self.board = deepcopy(object.board)
		self.height = object.board_height
		self.width = object.board_width




	def best_move (self,depth,state,current_player):
		queue = {}
		# current_player == 2
		# opp_player = 1
		if current_player == 1:
			opp_player = 2
		else:
			opp_player = 1

		for col in xrange(self.width):
			if is_legal(state, col):
				temp = self.move_to(state,col,current_player)
				queue[col] =  -self.search(depth-1,temp, opp_player)

		best_alpha = -999999
		best_Move = None
		moves = queue.items()
		
		random.shuffle(moves)
		#print moves , "this is list of moves"
		for move, alpha in moves:
			if alpha >= best_alpha:
				best_alpha = alpha
				best_Move = move

		return best_Move, best_alpha
		# make a move
		# return new board
		# do not alter the original board !!!!


		# must pass state instead of currrent board. 
		### change search, vertical , hori , diagonal ....
		#################
		# after that 
		# do main file 
		# while (game_over)
		# read input ,
		# call best move 
		# fix best move to json file.

	def search(self, depth, state, current_player):
		queue = []
		for i in xrange(self.width):
			if is_legal(state, i):
				temp = self.move_to(state,i,current_player)
				queue.append(temp)

		if depth == 0 or len(queue) == 0 or game_over(state):
			
			return self.cal_value(state,current_player)

		if current_player == 1:
			opp_player = 2
		else:
			opp_player = 1 
		alpha = -99999
		for node in queue:
			if node == None:
				print "it is empty"
			alpha = max(alpha, -self.search(depth-1,node,opp_player))
		return alpha

		# calculate value of each move
		# using heuristic function 
		# heuristic: 
		# 4streak = count *4
		# 3streak = count *3
		# 2streak = count *2
		# return sum of AI and sum of opponent 
	def cal_value(self,state,current_player):
		if current_player == 2:
			opp_player =1
		else:
			opp_player =2
		AI = []
		opp = []
		AI4 = (self.streak_counter(state,current_player,4))
		AI3 = (self.streak_counter(state,current_player,3))
		AI2 = (self.streak_counter(state,current_player,2))

		# for i in xrange(2,5):
		# 	AI.append((self.streak_counter(state,current_player,i)) * (10**i))
		opp = (self.streak_counter(state,opp_player,4))
		if opp > 0:
			return -1000
		else:
			return (AI4 *1000 + AI3*100 + AI2)

	# simulate a move . return a new state 
	
	def move_to(self,state, colum, color):
		temp = deepcopy(state)
		for i in xrange(self.height-1, -1,-1):
			if temp[colum][i] == 0:
				temp[colum][i] = color
				return temp


	# count total streak at current board
	# might have problem with passing the whole object vs 
	# passing the board. 
	def streak_counter(self,state,color,streak):
		count = 0
		for i in xrange(self.width):
			for j in xrange(self.height):
				if state[i][j] == color:
					count += self.vertical_streak_count(i, j,state, streak)
					count += self.horizontal_streak_count(i, j,state, streak)
					count += self.diagonal_streak_count(i, j,state,  streak)
				
		return count


	# return 1 if found streak 
	# diagonal return either 1 or 2 
	# cuz positive and negative slope.
	def vertical_streak_count(self, w,h,state, streak):
		consecutive_count = 0
		if h - streak - 1 > -1:
			for i in xrange(streak):
				if state[w][h] == state[w][h-i]:
					consecutive_count += 1
				else:
					break

		return 1 if consecutive_count == streak else 0
	# must count the negative 

	def horizontal_streak_count(self,w,h,state,streak):
		consecutive_count = 0
		if w + streak - 1 < self.width:
			for i in xrange(streak):
				if state[w][h] == state[w+i][h]:
					consecutive_count += 1
				else:
					break
			
		return 1 if consecutive_count == streak else 0

	# def negative_horizontal_streak_count(self,w,h,state,streak):
	# 	consecutive_count = 0
	# 	if w - streak + 1 > 0:
	# 		for i in xrange(streak):
	# 			if state[w][h] == state[w-i][h]:
	# 				consecutive_count += 1
	# 			else:
	# 				break
			
	# 	return 1 if consecutive_count == streak else 0

	def diagonal_streak_count(self,w,h,state,streak):
		# positive slope
		count = 0
		consecutive_count = 0
		if w + streak - 1 < self.width and h - streak -1 > -1:
			for i in xrange(streak):
				if state[w][h] == state[w+i][h-i]:
					consecutive_count += 1
				else:
					break
		if consecutive_count == streak:
			count += 1 

		consecutive_count = 0
		if w + streak - 1 < self.width and h + streak -1 < self.height:
			for i in xrange(streak):
				if state[w][h] == state[w+i][h+i]:
					consecutive_count += 1
				else:
					break
		if consecutive_count == streak:
			count += 1 
		return count




