from itertools import permutations

def getCoor(r,c,s):
    return (r-s-1, c-s-1, 2*s+1)

def copyBoard(src):
    return [row[:] for row in src]

def rotate(coor, board):
    nx, ny, w = coor
    
    while w>1:
        ansboard = copyBoard(board)
        for (dx, dy) in [(0,1), (1,0), (0, -1), (-1, 0)]:
            for _ in range(w-1):
                ansboard[nx+dx][ny+dy] = board[nx][ny]
                nx, ny = nx+dx, ny+dy
        w-=2
        nx, ny = nx+1, ny+1
        board = copyBoard(ansboard)
    return board
    
def getRowSum(board):
    return min(map(sum, board))

N, M, K = map(int, input().split())
original = [list(map(int, input().split())) for _ in range(N)]
operator = [list(map(int, input().split())) for _ in range(K)]
ans = 2e20

for p in permutations(range(K), K):
    board = copyBoard(original)
    for idx in p:
        r, c, s = operator[idx]
        board = rotate(getCoor(r,c,s), board)
    ans = min(ans, getRowSum(board))

print(ans)