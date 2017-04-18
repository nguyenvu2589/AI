from board import *

def is_full(state):
	return (0 in np.array(state))
# check for winning position. 
def is_connect_four(state):
	
	for i in xrange(len(state) - 1):
		for j in xrange(len(state[0]) - 1, -1,-1):

			if state[i][j] != 0:
				if check_vertical_four(state,len(state),i, j):
					return True, "vertical",i,j
				if check_horizontal_four(state,len(state),i, j):
					return True,"horizontal",i,j
				if check_diagonal_four(state,len(state), len(state[0]), i, j):
					return True,"diagonal",i,j
	return False, "good"
	
def check_vertical_four(board, width,w , h):
	count = 0
	if h - 3 > 0:
		for i in xrange(4):
			if board[w][h] == board[w][h -i]:
				count += 1
			else:
			    break
		# define the winner
		return True if count == 4 else None
	return False

def check_horizontal_four(board, width, w, h):
	count = 0
	if w +3 < width:
		for i in xrange(4):
			if board[w][h] == board[w+i][h]:
				count += 1
			else:
			    break
		# define the winner
		return True if count == 4 else None 
	return False

def check_diagonal_four(board, width,height, w, h):
	# positive slope
	count = 0
	if w +3 < width and h -3 > 0:
		for i in xrange(4):
			if board[w][h] == board[w+i][h-i]:
				count += 1
			else:
			    break
		# define the winner
		return True if count == 4 else None
	# negative slope
	count =0
	if w+3 < width and h+3 < height :
		for i in xrange(4):
			if board[w][h] == board[w+i][h+i]:
				count += 1
			else:
			    break
		# define the winner
		return True if count == 4 else None
	return False

# main check function ############
# 1. check if board is full -> 
# 2. Check if  winner found -> return True, and position ( w,h, winner)
# find winner by board[w][h]. 
def game_over(state):
	if not is_full(state):
		print "No more move"
	a = is_connect_four(state)
	if a[0]:
		return True ,a 
	return False


# return True if there is legal move to make
# return False if it is full.
def is_legal(state, colum):
	return True if 0 in state[colum] else False
	
		
