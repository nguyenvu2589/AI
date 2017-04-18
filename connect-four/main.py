from board import *
from AI import *
import sys
from random import randrange
import json
import time

def main():
	# #test board
	# input = {"grid":[[0,0,0,0,1,2],
	# 				 [0,0,0,0,1,2],
	# 				 [0,0,0,0,0,0],
	# 				 [0,0,0,0,0,0],
	# 				 [0,0,0,0,1,2],
	# 				 [0,0,0,0,0,1],
	# 				 [0,0,0,1,1,1]],"height":6,"player":1,"width":7}
	# finish_input ={"grid":[[0,2,2,1,2,1],[1,1,1,2,2,2],[1,2,2,1,2,1],[2,2,1,1,2,1],[2,1,2,2,1,1 ],[1,2,1,1,2,2],[1,2,1,2,1,1]],"height":6,"player":1,"width":7}
	
	# play manually
	# p1 = board(input)
	# ai = AI(p1)
	# bestmove, test = ai.best_move(4, p1.board,2)
	# print type(bestmove)

	# move = {"move":bestmove, "alpha": test}
	# print type(move)
	# print json.dumps(move)

	###### RUN THIS FOR DRIVER.
	###### DONE !!!!
	
	while(True):
		data = input()
		p1 = board(data)
		ai = AI(p1)
		bestmove, test = ai.best_move(2, p1.board,2)
		move = {"move":bestmove}
		print json.dumps(move)
		sys.stdout.flush()
		
		

	# for _ in range(10):
	# 	i = randrange(0,7)
	# 	print json.dumps({"move": i})
	# 	sys.stdout.flush()
	# 	time.sleep(1)

if __name__ == "__main__":
	main()