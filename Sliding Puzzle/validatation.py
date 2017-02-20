import numpy as np

def validation (data):
	# field check:
	assert data.keys()[0] == "start", "field start does not exist"
	assert data.keys()[1] == "goal","field goal does not exist"
	assert data.keys()[2] == "n", "field n does not exist"
	
	# n must be > 1	
	assert int(data.values()[2]) > 1 , "n < 1"

	# The start and goal fields must be n x n matrices
	assert (len(data["goal"]) == len(data["start"]) 
		== int(data.values()[2]) ), "do not have n x n matrix"

	# containing the integers 0 (for the empty space) to n2-1
	maxVal = int(data.values()[2]) ** 2 -1
	assert (np.max(data["start"], axis=(1,0)) ==
		np.max(data["goal"], axis=(1,0)) == maxVal)

	# min val is 0. 
	assert (np.min(data["start"], axis=(1,0)) ==
		np.min(data["goal"], axis=(1,0)) == 0)

	# no duplicate value 
	assert ([x for x in data['goal'] if data['goal'].count(x) == 1]), "duplicate value"
	