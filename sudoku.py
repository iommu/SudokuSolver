# This python file is to test the implementation of a custom sudoku solving algorithm. If sucessfull
# it will be converted into a C library 
# Author : Alex Carter (iommu)

import numpy as np

def display(puzzle):
    for i in range(0,9):
        for j in range(0,9):
            print(puzzle[i][j],end=" ")
            if j==2 or j==5:
                print('|',end=" ")
        print()
        if i==2 or i==5:
            print('- '*11)
        

def solve(puzzle):

    valid = np.full((9,9),511,dtype=np.uint16) # create 9x9 2d array of uint16s with value 511
    # 511 is decimal representation of 111111111 (9 1's) where each "1" represents a possible position for 9-->1

    bitAND = np.uint16(0) # this is an initial uint that will be used for bitwise and of the row and column

    def wipeCartesian(x,y):
        for i in range(0,9):
                valid[x][i] = valid[x][i]&bitAND # generate valid on x axis
                valid[i][y] = valid[i][y]&bitAND # generate valid on y axis

    def wipeTile(x,y):
        xOffset = x % 3
        yOffset = y % 3
        for i in range(x-xOffset,x-xOffset+3):
            for j in range(y-yOffset,y-yOffset+3):
                valid[i][j]=valid[i][j]&bitAND

    # Cross off initial possible positions
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j]:
                valid[i][j]=0
                bitAND = 2**(puzzle[i][j]-1) # calculate 2^(currentPosition-1), stored as uint16 i.e. 4 --> 2^(4-1) = 8 = ...0001000
                bitAND = ~bitAND # invert bitAND to create mask
                wipeCartesian(i,j)
                wipeTile(i,j)
                
    # Cyclicly fill in calculated positions for numbers 1-->9 until all positions solved
    solved = 1 # If no new solutions are found in a loop then the solver is stuck and should quit instead of repeating
    while solved:
        solved=0
        for tileX in range(0,3):
            for tileY in range(0,3):
                exclusive = [0,0,0,0,0,0,0,0,0]
                for positionX in range(0,3):
                    for positionY in range(0,3):
                        for value in range(0,9):
                            exclusive[8-value] += valid[tileX*3+positionX][tileY*3+positionY]>>(8-value)&0b1
                for value in range(0,9):
                    if exclusive[value]==1:
                        solved+=1
                        for positionX in range(0,3):
                            for positionY in range(0,3):
                                if valid[tileX*3+positionX][tileY*3+positionY]>>value&0b1:
                                    puzzle[tileX*3+positionX][tileY*3+positionY]=value+1
                                    valid[tileX*3+positionX][tileY*3+positionY]=0
                                    bitAND = 2**value
                                    bitAND = ~bitAND
                                    wipeCartesian(tileX*3+positionX,tileY*3+positionY)

    return puzzle