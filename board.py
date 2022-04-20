#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Kit Chung Yan
# email: kyan@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Cory Castle
# partner's email:ccastle@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[3*r + c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
        
    ### Add your other method definitions below. ###
    #Function 2
    def __repr__(self):
        """returns a string representation of a Board object"""
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    s += '_'
                else:
                    s += self.tiles[r][c]
                s += ' '
                
            s += '\n'
        return s
    #Function 3
    def move_blank(self, direction):
        """takes a input string direction specify which direction the blank 
        would move and the board is to be modify according to the direction 
        given. Result should return True or False to see if the move was 
        possible.
        """
        r1 = self.blank_r
        c1 = self.blank_c
        s= ''
        if direction == 'right':
            if c1 == 2:
                return False
            else:
                s += self.tiles[r1][c1+1]
                self.tiles[r1][c1+1] = self.tiles[r1][c1]
                self.tiles[r1][c1] = s
                self.blank_c += 1
                return True
        if direction == 'left':
            if c1 == 0:
                return False
            else:
                s += self.tiles[r1][c1-1]
                self.tiles[r1][c1-1] = self.tiles[r1][c1]
                self.tiles[r1][c1] = s
                self.blank_c -= 1
                return True
        if direction == 'up':
            if r1 == 0:
                return False
            else:
                s += self.tiles[r1-1][c1]
                self.tiles[r1-1][c1] = self.tiles[r1][c1]
                self.tiles[r1][c1] = s
                self.blank_r -= 1
                return True
        if direction == 'down':
            if r1 == 2:
                return False
            else:
                s += self.tiles[r1+1][c1]
                self.tiles[r1+1][c1] = self.tiles[r1][c1]
                self.tiles[r1][c1] = s
                self.blank_r += 1
                return True
        else:
            return False
    #Function 4
    def digit_string(self):
        """returns a string of digits that corresponds to the current contents 
        of the Board object’s tiles
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '_':
                    s += '0'
                else:
                    s += self.tiles[r][c]
        return s
    #Function 5
    def copy(self):
        """returns a new Board object which is a deep copy of Self board
        """
        return Board(self.digit_string())
    #Function 6
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object 
        that are not where they should be in the goal state
        """
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    if self.tiles[r][c] == '0':
                        count += 0 
                    else:
                        count += 1
        return count
                
        
    #Function 7
    def __eq__(self, other):
        """returns True if the called object (self) and the argument (other) 
        have the same values for the tiles attribute, and False otherwise
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False
    
        
    