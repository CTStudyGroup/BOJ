from collections import deque

def check(x, y, d, t): # check index range
    if t==2: y+=1
    elif t==3: x+=1
    
    if d == 'blue':
        return 0<=x<4 and 0<=y<10
    return 0<=x<10 and 0<=y<4

def isValid(board, x, y, t, d): # check board
    blocks = {1: [(x, y)], 2: [(x, y), (x, y+1)], 3:[(x, y), (x+1, y)]}
    for nx, ny in blocks[t]:
        if board[nx][ny]!=0:
            return False
    return True

def moveBlock(board, bpos, n, d):
    t, x, y = bpos
    direction = {'green': (1, 0), 'blue':(0, 1)}
    queue = deque([(x, y)])
    dx, dy = direction[d]

    while queue: # move
        cx, cy = queue.popleft()
        nx, ny = (cx + dx), (cy + dy)

        if check(nx, ny, d, t) and isValid(board, nx, ny, t, d):
            queue.append((nx, ny))

    fx, fy = nx-dx, ny-dy
    blocks = {1: [(fx, fy)], 2: [(fx, fy), (fx, fy+1)], 3:[(fx, fy), (fx+1, fy)]}
    for cx, cy in blocks[t]: # color blocks
        board[cx][cy] = n
    return board

def synchronize(board, rowNum, d):
    if d == 'green':
        board[rowNum][0:4] = [0]*4
        for i in range(rowNum, 4, -1):
            board[i][0:4] = board[i-1][0:4]

    elif d == 'blue':
        for j in range(0,4):
            board[j][rowNum] = 0 
        for i in range(rowNum, 4, -1):
            for j in range(0,4):
                board[j][i] = board[j][i-1]
    return board

def updateBlock(board):
    score = 0
    # get score
    for i in range(6,10): 
        if 0 not in board[i][0:4]: # row - green
            score += 1
            board = synchronize(board, i, 'green')

        if 0 not in [board[j][i] for j in range(0,4)]: # row - blue
            score += 1
            board = synchronize(board, i, 'blue')
    
    # remove row / column
    while board[5][0:4] != [0]*4: # row - green
        for i in range(9,3,-1):
            board[i][0:4] = board[i-1][0:4]
    
    while [board[j][5] for j in range(0,4)] != [0]*4: # row - blue
        for i in range(9,3,-1):
            for j in range(0,4):
                board[j][i] = board[j][i-1]
    return score, board

def numofBlocks(board):
    count = 0
    for i in range(10):
        count += sum(map(lambda x: x > 0, board[i]))
    return count

# input
board = [[0]*10 for _ in range(10)]
for i in range(4,10):
    board[i][4:10] = [-1] * 6
# solve
score = 0
N = int(input())
for n in range(1, N+1):
    bpos = list(map(int, input().split()))
    board = moveBlock(board, bpos, n, 'green')
    board = moveBlock(board, bpos, n, 'blue')
    s, board = updateBlock(board)
    score += s
print(score)
print(numofBlocks(board))