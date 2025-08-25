# ⚡️ 250825 : [BOJ 15653] 구슬 탈출 4

import sys

input = sys.stdin.readline
from collections import deque

d = [[0,1], [0,-1], [-1,0], [1,0]]

def move(r, b, choice, dir ) :
    if choice == 0 :  #빨간색 구슬 이동
        y, x = r
        
        while True :
            ty, tx = y + d[dir][0], x + d[dir][1]
            if board[ty][tx] == "O" :
                return ty, tx, 1
            if board[ty][tx] == "#" :
                return y, x, 0
            if ty == b[0] and tx == b[1] :
                return y, x, 0
            
            y, x = ty, tx
    else : 
        y, x = b
        while True :
            ty, tx = y + d[dir][0], x + d[dir][1]
            # if ty < 0 or ty >= N or tx < 0 or tx >= M :
            #     print("problem!! ", ty, tx)
            if board[ty][tx] == "O" :
                return ty, tx, 2
            if board[ty][tx] == "#" :
                return y, x, 0
            if ty == r[0] and tx == r[1] :
                return y, x, 0
            if board[ty][tx] == "O" :
                return ty, tx, 2
            y, x = ty, tx
            
def move_red_first(r, b, dir):
    r_new_y, r_new_x, flag1 = move(r, b, 0, dir)
    b_new_y, b_new_x, flag2 = move((r_new_y, r_new_x), b, 1, dir)
    return flag1 + flag2, (r_new_y, r_new_x), (b_new_y, b_new_x)


def move_blue_first(r, b, dir):
    b_new_y, b_new_x, flag1 = move(r, b, 1, dir)
    r_new_y, r_new_x, flag2 = move(r, (b_new_y, b_new_x), 0, dir)
    return flag1 + flag2, (r_new_y, r_new_x), (b_new_y, b_new_x)


def move_all(r, b, dir) :
    d = [[0,1], [0,-1], [-1,0], [1,0]]
    if dir == 0 :
        if r[1] >= b[1] :
            return move_red_first(r, b, dir)
        else :
            return move_blue_first(r, b, dir)
    if dir == 1 :
        if r[1]<b[1] :
            return move_red_first(r, b, dir)
        else :
            return move_blue_first(r, b, dir)
    if dir == 2 :
        if r[0] <= b[0] :
            return move_red_first(r, b, dir)
        else : 
            return move_blue_first(r, b, dir)
    if dir == 3 :
        if r[0] >= b[0] :
            return move_red_first(r, b, dir)
        else :
            return move_blue_first(r , b, dir)
def solve(r, b ) :
    q = deque()
    q.append((r, b,  0, -1))
    visited = set()
    visited.add((r[0],r[1], b[0], b[1]))
    while q :
        
        red_q, blue_q, cnt, prev= q.popleft()
        base_r, base_b = red_q, blue_q
        # print(f'popped : {red_q} {blue_q} {cnt}')
        for dir_ in range(4) :
            if prev == dir_ : continue
            nry, nrx = base_r[0] + d[dir_][0], base_r[1] + d[dir_][1]
            nby, nbx = base_b[0] + d[dir_][0], base_b[1] + d[dir_][1]
            # if nry < 0 or nry >= N or nby < 0 or nry >= N or nrx < 0 or nrx >= M or nbx<0 or nbx >=
            if (nry, nrx, nby, nbx) in visited : continue
            if board[nry][nrx] == "#" and board[nby][nbx] == "#" :
                continue
            flag,tmp_red, tmp_blue = move_all(red_q, blue_q, dir_)
            
            if (tmp_red[0], tmp_red[1], tmp_blue[0], tmp_blue[1]) in visited:
                continue
            visited.add((tmp_red[0], tmp_red[1], tmp_blue[0], tmp_blue[1]))
            if flag == 2 or flag == 3 : continue
            if flag == 1 :
                print(cnt + 1)
                sys.exit()
            q.append((tmp_red, tmp_blue, cnt + 1, dir_))
    print(-1)
        
N, M = map(int, input().split())
board = []
for _ in range(N) :
    board.append(list(input()))

red,  blue = [], []
for i in range(N) :
    for j in range(M) :
        if board[i][j] == "R" :
            red = [i, j]
            board[i][j] = "."
        if board[i][j] == "B" :
            blue = [i, j]
            board[i][j] = "."
            
solve( red, blue)
