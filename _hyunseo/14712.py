
def check(board, n) :
    y, x = n //M, n % M
    for dy in (0, -1):
        for dx in (0, -1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N-1 and 0 <= nx < M-1:
                if board[ny][nx] == 1 and board[ny+1][nx] == 1 and board[ny][nx+1] == 1 and board[ny+1][nx+1] == 1:
                    return True
    return False

def backtrack(n, board) :
    global answer
    if n >=  N*M :
        answer += 1
        return
    board[n//M][n%M] = 1
    if not check(board, n) :
        backtrack(n+1, board)
    board[n//M][n%M] = 0
    backtrack(n+1, board)
    
N, M = map(int, input().split())
board = [[-1]*M for _ in range(N)]

answer = 0

backtrack(0, board)
print(answer)
