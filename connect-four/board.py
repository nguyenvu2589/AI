import json
import numpy as np
from check_status import *

class board:
	def __init__(self,input):
		self.player = input['player']
		self.board = input['grid']
		self.board_height = input['height']
		self.board_width = input['width']
		

	def print_state():
		print "wat da ...."
		