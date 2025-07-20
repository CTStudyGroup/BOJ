
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []
for _ in range(N) :
    board.append(list(input().strip()))
print(board)

goal_word = list(input().strip())
print("dddddddddddd", goal_word, len(goal_word))
answer = 0

def move(y,x):
    d = [[1,0],[0,1],[-1,0],[0,-1]]
    paths = []
    for j in range(4) :
        for i in range(1, K+1) :
            ny, nx = y + d[j][0] * i, x + d[j][1]* i
            if 0<=ny<N and 0<=nx<M :
                paths.append([ny,nx])
    return paths


def backtrack(path, idx, y, x) :
    global answer
    print(path)
    if idx == len(goal_word) -1:
        answer += 1
        return
    if idx >= len(goal_word) :
        return
    next_alphabets = move(y,x )
    # 후보군 탐색
    for next_alphabet in next_alphabets :
        py, px = next_alphabet
        #가지치기
        if board[py][px] != goal_word[idx+1] : continue
        # 상태 변경
        path.append(board[py][px])
        backtrack(path, idx + 1,  py, px)
        #상태 복원
        path.pop()
        
for yy in range(N) :
    for xx in range(M) :
        if board[yy][xx] == goal_word[0] :
            backtrack([board[yy][xx]],0, yy, xx)
print(answer)
