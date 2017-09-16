#
#- If the cell is alive: if it has 2 or 3 alive neighbors, it stays alive. Otherwise, it dies.
#- If the cell is dead: if it has exactly 3 alive neighbors, it becomes alive. Otherwise, it stays dead.
#- The state of each cell is determined only by the state of its neighbors in the last iteration.

# live neighbor will be represented by 1,3
# dead neighbor will be represented by 0,2



# board : List[List[int]]

'''
def readBoardFromFile(board):
    while file_contents:
    Read the file partially load in into a 64MB chunk
    run the gameoflife() algorithm and write it to new file

    0 0 0 0
    0 0 0 0
    0 0 0 0
    0 0 0 0

    3x3 of the above chunk
'''

def liveNeighbors_for(board,r,c,i,j):
    count = 0
    for ii in xrange(max(i-1,0),min(i+2,r)):
        for jj in xrange(max(j-1,0),min(j+2,r)):
            count += board[ii][jj]

    count -= board[i][j]
    return count

def liveNeighbors(board,r,c,i,j):
    count = 0
    if i-1 >=0 and j-1 >=0:
        count += board[i-1][j-1]
    if i-1 >=0:
         count += board[i-1][j]
    if i-1 >=0 and j+1 < c:
        count += board[i-1][j+1]
    if j-1 >=0:
         count += board[i][j-1]
    if i+1 < r and j-1 >=0:
        count += board[i+1][j-1]
    if j+1 < c:
         count += board[i][j+1]
    if i+1 < r:
        count += board[i+1][j]
    if i+1 < r and j+1 < c:
        count += board[i+1][j+1]

    return count

def gameOfLife(board):
    ret_board = []

    r,c = len(board),len(board[0])

    ret_board = [board[i][:] for i in xrange(r)]

    for i in xrange(r):
        for j in xrange(c):
            lives = liveNeighbors_for(board,r,c,i,j)
            if board[i][j] == 0:
                if lives == 3:
                    ret_board[i][j] = 1
            else:
                if lives < 2 or lives > 3:
                    ret_board[i][j] = 0

    return ret_board


if __name__ == "__main__":
    '''
    1 0 0  0 0 0
    0 1 0  1
    0 1 1
    '''
    board = [[1,0,0],[0,1,0],[0,1,1]]

    new_board = gameOfLife(board)
    print new_board
