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
# solving alg
def solve(b):
    find = find_empty(b)
    if not find:
        return True
    else:
        r, c = find

    # loop 9 times
    for i in range(1, 10):
        # check if 
        if valid(b, i, (r,c)):
            b[]




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

pr_board(board)


# find empty positions in board and output their coordinates
def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == 0:
                return (i,j)
    return None
