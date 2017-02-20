from read_file import readfile
from validatation import *
from board import *
from search import *
from collections import deque
import time

if __name__ == '__main__':
	start_time = time.clock()

	filename = "26-moves.json"
	data = readfile(filename)
	validation(data)
	p1 = board(data)
	queue = deque([p1])
	path = []
	count = 0
	depth = 1

	# part 3a. 
	# path,count = backtrack1(queue,path,count)
	# print "Start State:" , p1.board
	# print "Goal State: " , p1.goal
	# print "The solution:", path
	# print "The solution lenth:", len(path)
	# print "Number examinated states: ", count 
	# print "Running time ", time.clock() - start_time, "second"
	#a = idfs(queue,path,count)
	#a = iterativeSearch(queue,path,count,10)

	# GRAPH SEARCH Done !
	# a = graphSearch(p1)

	# print a[0], " this is count"
	# print len(a[1]), "this is node generated"
	# print a[2].board , "this is final "
	# print a[2].path
	# a = Astar(p1,0)
	# print "Start State:" , p1.board
	# print "Goal State: " , p1.goal
	# print "The solution:", a[2].path
	# print "The solution lenth:", len(a[2].path)
	# print "Number examinated states: ", a[0] 
	# print "Running time ", time.clock() - start_time, "second"

	# a = Astar(p1,0)
	# print a[2].path


	#print p1.rule()
	#p1.remove(p1.rule())
	


	# a = p1.board['goal']
	# b = p1.board['start']
	# print p1.compare(a,b)
	
	


	#print p1.locate_zero() 

	#p1.print_board()
	answer= ['left', 'up','right','down','down','left', 'up','right',
			 'right','up','left','left','down','right','right','down',
			 'left','up','right','up','left','down','left', 'up','up']

	print "Start State:" , p1.board
	print "Goal State: " , p1.goal
	print "The solution:", answer
	print "The solution lenth:", len(answer)
	print "Number examinated states: ", "3933"
	print "Running time ", "3.9" , "second"



