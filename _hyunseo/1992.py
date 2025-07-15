# 흰점 0 검은 점 1 
import sys
input = sys.stdin.readline

'''
    board.append(list(map(int, input())))
                 ^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '\n' 
'''
#1 <= <= 64
N = int(input())
board = []
for _ in range(N) :
    board.append(list(map(int, input().strip())))
print(board)  
# 다 같은 수이면 그 수(1, 0) 반환, 아니면 -1 반환
def check(y,x,n) :
    base = board[y][x]
    if n == 1 :
        return base
    for i in range(n) :
        for j in range(n) :
            # print(y + i, x + j)
            if board[y + i][x+j] != base :
                return -1
    return base

answer =''

# 돌 방향
d = [[0,0], [0,1], [1,0], [1,1]]

def dfs(y, x, n ) :
    global answer
    # print(f'dfs entering with y : {y} x : {x} n : {n}')
    t = check(y, x, n)
    if t == 0 or t == 1 :
        answer += str(t)
    else :
        answer += "("
        for i in range(4) :
            dfs(y + d[i][0] * n//2, x + d[i][1] * n//2, n//2  )
        answer += ")"
dfs(0,0,N)
print(answer)
