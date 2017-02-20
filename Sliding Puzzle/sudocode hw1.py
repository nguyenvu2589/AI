
# DATALIST has to be a list or queue to store, previous path.
BACKTRACK1(DATALIST)
# DATAlist : starting state. 
# Data : current state
1 DATA ← FIRST(DATALIST);
DATALIST is a list of all databases back to the initial one. DATA is the most recent one produced.

# check current state with datalist traverse. 
# if match : repeat , return fail -> no solution.
# for item in datalist: 
# if compare( data, item ):
#	return fail

2 if MEMBER(DATA, TAIL(DATALIST)), return FAIL; 
the procedure fails if it revisits an earlier database.
# if compre ( new , goal)
	# return null

# Solution found.
3 if TERM(DATA), return NIL

# check number of possible move < BOUND 
# maybe < 4

# if len( datalist )> bound 
#	return fail
# BOUND is max number of steps
5 if LENGTH(DATALIST) > BOUND, return FAIL;
the procedure fails if too many rules have been applied. 
BOUND is a global variable specified before the procedure is first called.

# check for possible rule from data state
# add them to list RULE.
6 RULES ← APPRULES(DATA)

# now , LOOP through RULE file. 
# if it  empty -> return fail. 
# cant find solution
# for item in rules:
#	if len(rule) == 0
#		return fail
7 LOOP: 
	if NULL(RULES), return FAIL
	# pick first item in RULE, add to R
	8 R ← FIRST(RULES)
	# reduce the RULE size after pick 1.
	9 RULES ← TAIL(RULES)
	# make a move from R.
	# create a new databases
	# generate new board.
	10 RDATA ← R(DATA)
	

	# add new state to DATALIST. 
	# after generate newboard , add them to datalist.
	# datalist holds visited move.

	11 RDATALIST ← CONS(RDATA, DATALIST);
	the list of databases visited so far is extended by adding RDATA.
	
	# call recursively on new data
	# store the current path , by add move to PATH list
	12 PATH ← BACKTRACK1(RDATALIST)
	## if it return fail,
	# continue  for loop.

	13 if PATH = FAIL, go LOOP
	else:
	# else rerurn path. 
	14 return CONS(R, PATH)

# RULE : 
# check valid move : 
# 



Procedure GRAPHSEARCH
1 Create a search graph, G, consisting solely of the start node, s. 
Put s on a list called OPEN.
OPEN = G.pop()


2 Create a list called CLOSED that is initially empty.
CLOSED = []

3 LOOP: 
if OPEN is empty, exit with failure.
if len(OPEN) == 0:
	return False

4. Select the first node on OPEN, 
remove it from OPEN, and put it on CLOSED. 
Call this node n.

	n = OPEN.popleft()
	CLOSED.append(n)

5. if n is a goal node. 
Exit successfully with the solution obtained by 
tracing a path along the pointers from n to s in G. 
(Pointers are established in step 7.)
	if n.is_goal():
		return path

6. Expand node n, generating a set, M, 
of its successors and install them as successors of n in G.
# create new boards by calling moves ?



7. Establish a pointer to n from those members of M that 
were not already in G (i.e., not already on either OPEN or CLOSED). 
Add these members of M to OPEN. For each member of M that is already 
OPEN or CLOSED, decide whether or not to redirect its pointer to n. 
For each member of M already on CLOSED, decide for each of 
its descendents in G whether or not to redirect its pointer.

8 Reorder the list OPEN, either according to some arbitrary scheme 
or according to heuristic merit.

9 Go LOOP

