'''
사과 먹으면 뱀 늘어남
뱀이 벽 or 자기 자신과 부딪히면 게임 끝


NxN 보드위에서 진행, 사과가 놓여져 있고, 상하좌우에 벽
벽은 맨위맨좌에서 시작(0,0) 뱀의 길이는 1
처음은 오른쪽을 향해 감 ->

매초마다 이동
1. 몸 길이를 느려 머리를 다음칸에 위치
2. if 머리가 벽 or 자기 자신 -> 게임 끝!!!
3. 만약 이동한 칸에 사과 -> 사과 먹음.
4. 만약 이동한 칸에 사과 X -> 몸 길이 줄여. 꼬리 줄여. 

'''

import sys
from collections import deque

d = [[0,1], [1,0], [0,-1], [-1,0]]

def solve() :
    time = 0
    dir = 0   # 처음 방향은 0, 오른쪽
    snake = deque()
    snake.append([0,0])
    while True :
        time += 1
        # 1. 몸 길이 늘림.
        new_head = [snake[-1][0] + d[dir][0], snake[-1][1] + d[dir][1]]
        
        if new_head[0] < 0 or new_head[0] >= N or new_head[1] < 0 or new_head[1] >= N :
            print(time)
            sys.exit()
        if board[new_head[0]][new_head[1]] == 2 :
            print(time)
            sys.exit()  # 자기 자신 만남
        
        if board[new_head[0]][new_head[1]] == 0 : # 사과 없음
            tmp = snake.popleft()
            board[tmp[0]][tmp[1]] = 0  # 줄어듬
        
        board[new_head[0]][new_head[1]] = 2
        snake.append(new_head)
        
        
        if time in move_dic.keys() :
            dir += move_dic[time]
        dir = dir % 4
        
        

N = int(input())  # 보드 크기
K = int(input())  # 사과 개수

board = [[0]*N for _ in range(N)]

for _ in range(K) :
    y, x = map(int, input().split())
    board[y-1][x-1] = 1
    
board[0][0] = 2

L = int(input())  # 방향 변환 횟수
move_dic = {}
for _ in range(L) :
    X, C = map(str, input().split())
    if C == 'L' :
        move_dic[int(X)] = -1
    else :
        move_dic[int(X)] = 1
    # X초가 끝난 뒤에 L은 dir을 -1, D는 +1
solve()
