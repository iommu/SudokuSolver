
import sudoku

puzzle =    [[0,0,0,0,0,0,0,0,7],
             [8,7,0,0,2,0,0,0,6],
             [9,0,0,0,1,6,0,2,8],
             [2,0,0,9,8,0,6,7,4],
             [0,0,6,1,0,2,8,0,0],
             [4,8,9,0,7,5,0,0,3],
             [5,2,0,4,3,0,0,0,9],
             [6,0,0,0,9,0,0,8,1],
             [1,0,0,0,0,0,0,0,0]]

sudoku.display(puzzle)
print("\n")
output = sudoku.solve(puzzle)
sudoku.display(output)