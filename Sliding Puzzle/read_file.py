import json
import numpy as np

# read file
def readfile(filename):
	with open(filename) as file:
		data = json.load(file)
	return data