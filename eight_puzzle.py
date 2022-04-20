#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name: Cory Castle
# partner's email: ccastle@bu.edu
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
def process_file(filename, algorithm, param):
    """ Takes Three Input:
        1. a string filename name of a text file in which each line is a digit 
        string for an eight puzzle
        2. a string algorithm specifying which search algorithm should be used
        to solve the puzzles ('random', 'BFS', 'DFS', 'Greedy', or 'A*')
        3. a input parameter param that specifies whether to use a depth limit 
        searcher or a choice of heuristic function
    """
    file = open(filename,'r')
    count = 0
    a = 0
    states = 0
    for line in file:
        line = line[:-1]
        board = Board(line)
        state = State(board, None, 'init')
        searcher = create_searcher(algorithm, param)
        try:
            s = searcher.find_solution(state)
            if s == None:
                print(line+':','no solution')
            else:
                count += 1
                a += s.num_moves
                states += searcher.num_tested
                print(line+':',s.num_moves,'moves,',searcher.num_tested,'states tested')
        except KeyboardInterrupt:
               print((line)+':','search terminated,', 'no solution')
               count += 0
    if count == 0:
        print('')
        print('solved',0,'puzzles')
    else:
        print('')  
        print('solved',count,'puzzles')
        print('averages:',(a/count), 'moves,',(states/count),'states tested')
    file.close
