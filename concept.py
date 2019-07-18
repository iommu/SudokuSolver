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

puzzle = [[1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]

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

# step 2 : crross off initial possible positions
for i in range(0,9):
    for j in range(0,9):
        if puzzle[i][j]:
            valid[i][j]=0
            bitAND = 2**(puzzle[i][j]-1) # calculate 2^(currentPosition-1), stored as uint16 i.e. 4 --> 2^(4-1) = 8 = ...0001000
            bitAND = ~bitAND # invert bitAND to create mask
            for k in range(0,9):
                valid[i][k] = valid[i][k]&bitAND # generate valid on x axis
                valid[k][j] = valid[k][j]&bitAND # generate valid on y axis

# debugger
for i in range(0,9):
    for j in range(0,9):
        print(format(valid[i][j],'09b')+" ",end="")
    print()
            

# step 3 :  Cyclicly fill in calculated positions for numbers 1-->9 until all positions solved

solved = 1 # If no new solutions are found in a loop then the solver is stuck and should quit instead of repeating
if solved:
    for i in range(1,10):
        print(i)    