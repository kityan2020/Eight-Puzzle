# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:28:50 2021

@author: Kit Chung Yan
"""

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return self.base*self.height*0.5
    def __repr__(self):
        return ('triangle with base'+ ' '+str(self.base)+' ' + 'and height' + ' ' +str(self.height))
    def __eq__(self, other):
        return self.base == other.base \
            and self.height == other.height
def main():
        tri1 = Triangle(3,4)
        tri2 = Triangle(6,6)
        tri3 = Triangle(3,4)
        print('tri1:', tri1 ,'(area =',str(tri1.area())+')')
        print('tri2:', tri2 ,'(area =',str(tri2.area())+')')
        print('tri3:', tri3 ,'(area =',str(tri3.area())+')')
        if tri1 != tri2:
            print('tri1 and tri2 are not equal')
        else:
            print('tri1 and tri2 are equal')
        if tri1 == tri3:
            print('tri1 and tri3 are equal')
        else:
            print('tri1 and tri3 are not equal')
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        b = side
        h = side *0.866
        super().__init__(b,h)
    def __repr__(self):
        s = ('equilateral triangle with side')
        s+= ' '
        s += str(self.base)
        return s
def uniquify(vals):
    if vals == []:
        return []
    else:
        uni_rest = uniquify(vals[1:])
        if vals[0] not in uni_rest:
            return [vals[0]] + uni_rest 
        else:
            return uni_rest
def merge(l1,l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    if l1 and l2 == []:
        return []
    else:
        merge_rest = merge(l1[1:],l2[1:])
        return [l1[0]] + [l2[0]] + merge_rest
def symmetric(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c+1] == grid[r+1][c]:
                return True
            else:
                return False