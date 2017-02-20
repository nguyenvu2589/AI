import numpy as np

def locate_zero(board):
		return zip(*np.where(np.array(board) == 0)) 

def rule(self):
	rules = []
	n = len(self. board[0])
	zero = locate_zero(self.board)
	row = zero[0][0]
	col = zero[0][1]
	
	# 1. ALL coner.
	# top left coner
	if (row, col) == (0,0): 
		rules.extend(("down", "right"))
	# top right coner
	elif (row, col) == (0,n-1): 
		rules.extend(("left","down"))
	# bottom left coner
	elif (row, col) == (n-1,0): 
		rules.extend(("up","right"))
	# bottom right coner
	elif (row, col) == (n-1,n-1): 
		rules.extend(("up", "left"))

	# 2. Top row
	elif ((row == 0) and (col in range(1, n-1))):
		rules.extend(("left", "down","right"))

	# 3. bottom row
	elif ((row == n-1) and (col in range(1, n-1))):
		rules.extend(("up", "right", "left"))

	# 4. Left Column 
	elif ((col == 0) and (row in range(1, n-1))):
		rules.extend(("up", "right","down"))
	# 5. Right Column
	elif ((col == n-1) and (row in range(1, n-1))):
		rules.extend(("up", "left","down" ))
	else:
		rules.extend(("up", "left", "down","right"))
	return rules

	# [1] 12 ..... 1n 
	# 21
	# .
	# .
	# n1 n2 ..... nn 

	