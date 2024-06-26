# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #use stack 
    frontier = util.Stack()  #frontier manages which states to expand 
    frontier.push((problem.getStartState(), [])) #empty list represents list of directions to goal state node
    expanded = []  # List to check whether state has already been visited/expanded
    #path_to_node = []
  
    while not frontier.isEmpty(): 
       # node = frontier.pop()  #put the current node from frontier into node  
        node, path_to_node = frontier.pop() #node is just the letter (A, B, etc), path_to_node is the list of directions
        if problem.isGoalState(node):
            return path_to_node
        if node not in expanded:
            expanded.append(node)
            for child, direction, cost in problem.getSuccessors(node):
               # frontier.append(child[0])
              # path_to_node.append(direction)   
                path_to_child = path_to_node + [direction]
                frontier.push((child, path_to_child))

    return False

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    #Start's successors: [('B', '0:A->B', 1.0), ('C', '1:A->C', 2.0), ('D', '2:A->D', 4.0)]
    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

     #USE A QUEUE 

    frontier = util.Queue()  #frontier manages which states to expand 
    frontier.push((problem.getStartState(), [])) #empty list represents list of directions to goal state node
    expanded = []  # List to check whether state has already been visited/expanded
    #path_to_node = []
  
    while not frontier.isEmpty(): 
       # node = frontier.pop()  #put the current node from frontier into node  
        node, path_to_node = frontier.pop() #node is just the letter (A, B, etc), path_to_node is the list of directions
        if problem.isGoalState(node):
            return path_to_node
        if node not in expanded:
            expanded.append(node)
            for child, direction, cost in problem.getSuccessors(node):
               # frontier.append(child[0])
              # path_to_node.append(direction)   
                path_to_child = path_to_node + [direction]
                frontier.push((child, path_to_child))

    return False



    #util.raiseNotDefined()

   

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    frontier = util.PriorityQueue()  #frontier manages which states to expand 
    frontier.push((problem.getStartState(), []), 0) #empty list represents list of directions to goal state node, 0 is the priority
    expanded = []  # List to check whether state has already been visited/expanded
  
    while not frontier.isEmpty(): 
       # node = frontier.pop()  #put the current node from frontier into node  
        node, path_to_node = frontier.pop() #node is just the letter (A, B, etc), path_to_node is the list of directions
        if problem.isGoalState(node):
            return path_to_node
        if node not in expanded:
            expanded.append(node)
            for child, direction, cost in problem.getSuccessors(node):
                path_to_child = path_to_node + [direction]
                gottenCost = problem.getCostOfActions(path_to_child) 
                frontier.push((child, path_to_child), cost + gottenCost) 

    return path_to_node
   #  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0




def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()  #frontier manages which states to expand 
    frontier.push((problem.getStartState(), [], 0), 0) #empty list represents list of directions to goal state node
    expanded = []  # List to check whether state has already been visited/expanded
  
    while not frontier.isEmpty(): 
        node, path_to_node, current_cost = frontier.pop() #node is just the letter (A, B, etc), path_to_node is the list of directions
        if problem.isGoalState(node):
            return path_to_node
        if node not in expanded:
            expanded.append(node)
            # maybe have a list of cumulative successors that have not been checked yet?
            # allSuccessors.push(problem.getSuccessors(node))
            for child, direction, cost in problem.getSuccessors(node):
                path_to_child = path_to_node + [direction]
                gottenCost = problem.getCostOfActions(path_to_child)  + heuristic(child, problem)
                frontier.push((child, path_to_child, current_cost + cost), current_cost + cost + heuristic(child, problem))
                   
    return path_to_node

    #priority queue 


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
