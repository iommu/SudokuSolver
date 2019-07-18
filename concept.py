# This python file is to test the implementation of a custom sudoku solving algorithm. If sucessfull
# it will be converted into a C library 
# Author : Alex Carter (iommu)

import numpy as np

# step 1 :  Import a 9x9 array
puzzle =    [[0,0,0,0,0,0,0,0,7],
             [8,7,0,0,2,0,0,0,6],
             [9,0,0,0,1,6,0,2,8],
             [2,0,0,9,8,0,6,7,4],
             [0,0,6,1,0,2,8,0,0],
             [4,8,9,0,7,5,0,0,3],
             [5,2,0,4,3,0,0,0,9],
             [6,0,0,0,9,0,0,8,1],
             [1,0,0,0,0,0,0,0,0]]

# 511 is decimal rep of 111111111 where each "1" represents a possible position for 9-->1
valid = np.uint16([
        [511,511,511,511,511,511,511,511,511],
        [511,511,511,511,511,511,511,511,511],
        [511,511,511,511,511,511,511,511,511],
        [511,511,511,511,511,511,511,511,511],
        [511,511,511,511,511,511,511,511,511],
        [511,511,511,511,511,511,511,511,511],
        [511,511,511,511,511,511,511,511,511],
        [511,511,511,511,511,511,511,511,511],
        [511,511,511,511,511,511,511,511,511]
])

# this is an initial uint that will be used for bitwise and of the row and column
bitAND = np.uint16(0)

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
# step 2 : crross off initial possible positions
for i in range(0,9):
    for j in range(0,9):
        if puzzle[i][j]:
            valid[i][j]=0
            bitAND = 2**(puzzle[i][j]-1) # calculate 2^(currentPosition-1), stored as uint16 i.e. 4 --> 2^(4-1) = 8 = ...0001000
            bitAND = ~bitAND # invert bitAND to create mask
            wipeCartesian(i,j)
            wipeTile(i,j)

# debugger
for i in range(0,9):
    for j in range(0,9):
        print(format(valid[i][j],'09b')+" ",end="")
    print()
            

# step 3 :  Cyclicly fill in calculated positions for numbers 1-->9 until all positions solved

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
            print(exclusive)
            for value in range(0,9):
                if exclusive[value]==1:
                    print("solving"+str(value))
                    solved+=1
                    print("solved = "+str(solved))
                    for positionX in range(0,3):
                        for positionY in range(0,3):
                            if valid[tileX*3+positionX][tileY*3+positionY]>>value&0b1:
                                puzzle[tileX*3+positionX][tileY*3+positionY]=value+1
                                valid[tileX*3+positionX][tileY*3+positionY]=0
                                bitAND = 2**value
                                bitAND = ~bitAND
                                wipeCartesian(tileX*3+positionX,tileY*3+positionY)
    print(solved)

print()
print()
for i in range(0,9):
    for j in range(0,9):
        print(format(valid[i][j],'09b')+" ",end="")
    print()

print()
print()
for i in range(0,9):
    for j in range(0,9):
        print(format(puzzle[i][j])+" ",end="")
    print()