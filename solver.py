# sudoku solver using a backtracking algorithm

# 9x9 board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# solving algorithm
# this only solves 1 empty space each time it is called
def solve(b):
    # takes the given empty space
    find = find_empty(b)
    # if there is no empty space in the board, return True to end the program
    if not find:
        return True
    else:
        # if there is, take its x, y coords
        r, c = find

    # loop through 1 - 9 and try each number 
    for i in range(1, 10):
        # check if it is valid, if it is, assign the number to that empty space
        if valid(b, i, (r,c)):
            b[r][c] = i

        # go to the next empty space and recursively try to solve the whole board until there is no more
        if solve(b):
            # this will only run if find is equal to False
            return True
        
        # if solve is equal to False revert the last coordinate to 0
        b[r][c] = 0        

    # if none of the values iterated in the for loop are valid
    return False

# checks if the position valid
# p is the tuple of function find_empty (x, y), n is the input number
def valid(b, n, p):
    # check row
    for i in range(len(b)):
        if b[p[0]][i] == n and p[1] != i:
            return False
        
    # check column
    for i in range(len(b)):
        if b[i][p[1]] == n and p[0] != i:
            return False
        
    # check boxes
    box_x = p[1] // 3
    box_y = p[0] // 3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if b[i][j] == n and (i, j) != p:
                return False
    
    return True
            
# prettify the board in the terminal
def pr_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print('— — — — — — — — — — — — ')
        #        range(0,9) to access the indices in the list
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + ' ', end='')


# find empty positions in board and output their coordinates
def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j)
    return None


pr_board(board)
solve(board)
pr_board(board)
