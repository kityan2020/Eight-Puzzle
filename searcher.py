#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Kit Chung Yan
# email: kyan@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Cory Castle
# partner's email: ccastle@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, depth_limit):
        """ constructs a new Searcher object by initializing an attributre
        states for the Searchers list of untested states to an empty list,
        an attribute num_tested to keep track keep track of how many states 
        the Searcher tests starting from 0 and a depth_limit to
        specify how deep the state-space search tree the Searcher will go
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    def add_state(self, new_state):
        """takes a single State object new_state and adds it to the 
        searchers list of untested states.
        """
        self.states += [new_state]
    def should_add(self, state):
        """takes a State object state and returns True if Searcher should add
        state to its list of untested states and returns False otherwise
        """
        if self.depth_limit != -1 and self.depth_limit < state.num_moves:
            return False
        if state.creates_cycle():
            return False
        else:
            return True
    def add_states(self, new_states):
        """ takes a list of state objects new__states, and processes 
        the elements of new_states one at a time with the following:
            1. if the given state s hould be added to the Searcher‘s list of 
            untested states 
            2. If a given state s should not be added to the Searcher object’s 
            list of states, the method should ignore the state.
        """
        for x in new_states:
            if self.should_add(x):
                self.add_state(x)
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    def find_solution(self, init_state):
        """ performs a full state-space search that begins at the init_state
        and ends when the goal state is found or when it runs out of untested
        states
        """
        self.add_state(init_state)
        while self.states:
            g = self.next_state()
            self.num_tested += 1
            if g.is_goal() == True:
                return g
            else:
                self.add_states(g.generate_successors())
            
        return None
    


### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
     """ A class for Searcher objects that performs breadth-first search
       instead of random search. BFS will choose the untested states that 
       will have the smallest depth
     """
     def next_state(self):
         """chooses the state that has been in the list the longest."""
         for s in self.states:
             self.states.remove(s)
             return s
class DFSearcher(Searcher):
    """ A class for Searcher objects that performs depth-first search instead
    of a random search. DFS will choose the state that has the largest depth 
    away from the initial state
    """
    def next_state(self):
        """chooses the state that has been in the list the longest."""
        state = self.states[::-1]
        for s in state:
            self.states.remove(s)
            return s
        
        
        
def h0(state):
        """ a heuristic function that always returns 0 """
        return 0
### Add your other heuristic functions here. ###
def h1(state):
    """ takes a State object state and returns the amount of moves needed from
    state to reach the goal state"""
    return state.board.num_misplaced()
def h2(state):
    """ a heuristic function that return the number of tiles misplaced in the
    state by row an column
    """
    count = 0
    for r in range(len(state.board.tiles)):
        for c in range(len(state.board.tiles[0])):
            if state.board.tiles[r][c] != GOAL_TILES[r][c]:
                if state.board.tiles[r][c] == '0':
                    count += 0
                else:  
                    count += abs(r-(int(state.board.tiles[r][c]) // 3)) 
                    count += abs(c-(int(state.board.tiles[r][c]) % 3))
    return count
                
            

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self,heuristic):
        """modifies the init constructor from Searcher class and replace the
        depth limit with -1 as it will not use a depth limit. It will 
        initialize a new attribute heuristic assigning whatever value is passed
        into the heuristic parameter
        """
        self.heuristic = heuristic
        super().__init__(-1)
        


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher"""
        return -1 * self.heuristic(state)
    def add_state(self, state):
        """ overrides the add_state method in Searcher class. Adds a sublist
        that is a [priority,state] pair where priority of state is determined
        by calling the priority method. It will allow GreedySearcher to choose
        the next state based on the priorities of the states.
        """
        self.states += [[self.priority(state),state]]
    def next_state(self):
        """ overrides the next_state method and chooses one of the states with
        the highest priority and return only the state component of the sublist
        and not the entire sublist
        """
        s = max(self.states)
        self.states.remove(s)
        return s[-1]


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """ A class object that performs a A* Search"""
    def __init__(self,heuristic):
        """modifies the init constructor from GreedySearcher class
        """
        super().__init__(heuristic)
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        return super().__repr__()
    def priority(self, state):
        """ ovverides the priority of Greedy class and returns the priority 
        of the specified state,
        based on the heuristic function used by the searcher and num_moves 
        of the state
        """
        return -1 * (self.heuristic(state) + state.num_moves)

        

