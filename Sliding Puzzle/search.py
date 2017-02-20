from board import *
from copy import deepcopy
from rule import rule
import itertools
from Queue import PriorityQueue

def backtrack1(queue,path,count):
	# copy the last item in queue.
	node = deepcopy(queue[-1])
	# check for prev moves. If so, return false

	if (len(queue)>1):
		for i in  range (len(queue) -1):
			if (compare(node,queue[i])):
				path.pop()
				return False,count
	#check if solution found.
	if node.is_goal():
		return path,count
	# Find legal move.
	rules = rule(node)
	if len(queue) > 2:
		return False, count
	while rules >=0 :
		count +=1
		if len(rules) == 0:
			return False,count

		# update new board
		newN = deepcopy(node)

		newN.moves(rules[0])
		newNode = deepcopy(queue)
		newNode.append(newN)

		# add to path
		path.append(rules[0])
		del rules[0]
		# call for result in new board.
		result,count = backtrack1(newNode, path,count)

		# if false, try different path.
		if result == False:
			continue
		else:
			# if found, return result.
			return path,count

# run from 1 to maxdepth.
# doesnt stop.

def iterativeSearch(queue,path,count,maxDepth):
	for i in range (maxDepth):
		print path , "long path"
		# path = []
		a = idfs(queue, path, count, i)
	return False


def idfs(queue,path,count,depth):
		# copy the last item in queue.
	node = deepcopy(queue[-1])
	# check for prev moves. If so, return false
	print len(queue), "this is len q"

	if (len(queue)>1):
		for i in  range (len(queue) -1):
			if (compare(node,queue[i])):
				path.pop()
				return False,count
	#check if solution found.
	if node.is_goal():
		return path,count
	# Find legal move.
	rules = rule(node)
	if len(queue) > depth:
		print "path"
		return "depth",count

	while rules >=0 :
		count +=1
		if len(rules) == 0:
			return "depth",count

		# update new board
		newN = deepcopy(node)
		print node.board, " this is board "
		newN.moves(rules[0])
		queue.append(newN)
		# newNode = deepcopy(queue)
		# newNode.append(newN)

		# node.moves(rules[0])
		# newNode = deepcopy(queue)
		# newNode.append(node)

		# add to path
		path.append(rules[0])
		del rules[0]
		# call for result in new board.
		result,count = backtrack1(queue, path,count)

		# if false, try different path.
		if result == False:
			continue
		if result == "depth":
			return queue,path,count
		else:
			# if found, return result.
			return queue,path,count, "true"

def graphSearch(root_node):
	count = 0 # Only for stats.
	visited = set()
	queue = PriorityQueue()
	# put because ..putting it priority in . 
	queue.put(root_node)

	# make move without changing the original node.
	#rerurn newNode
	def make_move(node,rule):
		newNode = deepcopy(node)
		newNode.moves(rule)
		newNode.path.append(rule)
		return newNode

		# find unvisted node. 
		# find all posible move 
		# genenrate new board for each move. 
		# check with visited state. 
		# if not in visited
		# add to  newNode.
	def unvisited_children(node):
		newNode = []
		# generate a list of moves. 
		for item in rule(node):
			newNode.append(make_move(node,item)) if make_move(node,item) not in visited else 0
		return newNode

		# if queue not empty.
		# copy 1 to node. 
		# mark it as visited. 
		# check for goal.
		# add all the child node from new node to queue.
	while not queue.empty():
		count +=1
		node = queue.get()
		visited.add(node)

		if node.is_goal():
			return (count, queue.queue, node)
		
		for item in unvisited_children(node):
			queue.put(item)
	return (count, queue)


def Astar(root_node, heuristic):
	count = 0 # Only for stats.
	visited = set()
	queue = PriorityQueue()
	# put because ..putting it priority in . 
	queue.put((0,root_node))

	# make move without changing the original node.
	#rerurn newNode
	def make_move(node,rule):
		newNode = deepcopy(node)
		newNode.moves(rule)
		newNode.path.append(rule)
		return newNode

	def priority(node):
		return (node.heuristic_sum(),node)
		# find unvisted node. 
		# find all posible move 
		# genenrate new board for each move. 
		# check with visited state. 
		# if not in visited
		# add to  newNode.
	def unvisited_children(node):
		newNode = []
		# generate a list of moves. 
		for item in rule(node):
			newNode.append(make_move(node,item)) if make_move(node,item) not in visited else 0
		return newNode

		# if queue not empty.
		# copy 1 to node. 
		# mark it as visited. 
		# check for goal.
		# add all the child node from new node to queue.
	while not queue.empty():
		count +=1
		node = queue.get()[1]
		visited.add(node)

		if node.is_goal():
			return (count, queue.queue, node)
		
		for item in map(priority,unvisited_children(node)):
			queue.put(item)
	return (count, queue)
