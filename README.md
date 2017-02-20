## Sliding-Tile Puzzle
A sliding-tile puzzle is a rectangular grid of tile with one empty space. You can slide a tile into an adjacent empty space. The object of the puzzle is to rearrange the tiles into a given goal state. Figure 1 shows a typical instance of the 8-puzzle, which uses a 3 x 3 grid.

For this assignment, we will limit ourselves to n x n sliding-tile puzzles, where n > 1. Such a puzzle has tiles numbered 1 to n2-1 plus the empty tile. For specific values of n, such puzzles are known as <n2-1>- puzzles. The most common are 8-puzzles and 15-puzzles.
In this assignment you will write a series of programs to solve sliding-tile puzzles using various uninformed and informed (heuristic) methods.


# Part 1 – Reading and Validating Sliding-Puzzle Problems
We will use JSON, which is described below, to define specific sliding-tile puzzle instances for your programs to solve. An example JSON corresponding to the instance of the 8-puzzle in Figure 1 is:
{"n" : 3,
 "start" : [[7,2,4],
           [5,0,6],
           [8,3,1]],
 "goal" : [[0,1,2],
           [3,4,5],
           [6,7,8]]}
This is an 8-puzzle problem with a grid size of n = 3 and the specified 3 x 3 matrices for the start state and the goal state. Each state is a 3 x 3 matrix of non-negative integers and the empty space is denoted by the integer 0.
 1

# Part 2 – Sliding-Tile Puzzle Rules
Given a sliding-tile puzzle state, you must be able to determine the rules that are applicable to that state that can be used to generate its successor states.
A rule has three parts:
-  name – a simple name for the rule (e.g., up, left, down, right)
- precondition function – a Boolean function that accepts a state and returns true if the rule is applicable to state
- action function – a function that accepts a state and returns the successor state obtained by applying the rule
You can use these rules to implement functions such as applicable-rule, which returns a list of the rules applicable to a given state, and successor-state, which returns the successor state for a given state and rule.
Encode the rules for the sliding-tile puzzle. Remember that it is easiest to consider moving the empty space up, left, down, or right. Using these rules, write routines to determine the rules applicable to a state and the successor state given a state and rule to apply.
Note that you could implement these as iterators or have them return lists (or vectors) or rules and states.

# Part 3 – Backtracking Control Strategy
Implement the BACKTRACK1(DATALIST) algorithm to solve instances of the sliding-puzzle problem. The depth bound may be a global variable or passed as an argument.
Implement a main program to accept a sliding-tile puzzle problem and solve it using the BACKTRACK1(DATALIST) algorithm. Print the start state and the goal state; the solution and solution length; and the number of states that were examined.
Implement a main program to accept a sliding-tile puzzle problem and solve it using an iterative depth- first search using the BACKTRACK1(DATALIST) algorithm. Print the cumulative number of states examined and the final (optimal) solution.

# Part 4 – Graph Search
Implement GRAPHSEARCH algorithm and use it to perform a breadth- first search of sliding-tile problems.
Implement a main program to accept a sliding-tile puzzle and solve it using your implementation. Print the start and goal state; the solution and solution length; and the number of states generated and explored.

# Part 5 – Algorithm A*
The most widely known form of best-first is called A* search (pronounced “A-star search”). It evaluates nodes by combining 𝑔(𝑛), the cost to reach the node, and h(𝑛), the cost to get from the node to the goal:
𝑓(𝑛) = 𝑔(𝑛) + h(𝑛).
Since 𝑔(𝑛) gives the path cost from the start node to node n, and h(𝑛) is the estimated
cost of the cheapest path from n to the goal, we have
𝑓(𝑛) = the estimated cost of the cheapest solution through n.
... The algorithm is identical to Uniform-Cost-Search except that A* uses g + h instead of g.
