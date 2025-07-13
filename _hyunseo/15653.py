# # 직사각형 보드에 빨간 구슬, 파란 구슬 하나씩, 
# # 빨간 구슬을 구멍을 통해 빼내는 게임

# #세로 크기 N, 가로 크기 M 
# N, M = map(int, input().split())

# #가장 바깥 행과 열은 모두 막혀 있고, 보드에는 구멍 하나
# # 하나의 칸에는 하나의 구슬

# # 구슬을 손으로 건드릴 수 잆고, 중력을 이리 저리 굴려야함
# # <- 아래 -> 위 이렇게 4가지 동작 가능
# # 공은 동시에 이동

# # 파란 구슬이 빠지면 실패, 파란 & 빨간 동시에 빠져도 실패 

# # 최소 몇번만에 구슬을 뺄 수 있는지 출력



##--------------------- 통과 못한 반례
# 6 6
# ######
# #R#BO#
# #....#
# ###..#
# #.#..#
# ######
# ------------------------------

#세로 크기 N, 가로 크기 M (3<=N, M<=10)
N, M = map(int, input().split())
import copy
# . 빈칸, # 벽 (이동 불가능), o 구멍. R 빨간 공, B 파란 공
# *** 한줄 코딩
board = [list(input().strip()) for _ in range(N)]
visited_set = set()

for i in range(N) :
    for j in range(M) :
        if board[i][j] == "B" :
            blue_x, blue_y = j, i
        if board[i][j] == "R" :
            red_x, red_y = j , i
            
visited_set.add((blue_x, blue_y, red_x, red_y))



# N,M = 5,5
# board = [['#', '#', '#', '#', '#'], ['#', '.', '.', 'B', '#'], ['#', '.', '#', '.', '#'], ['#', 'R', 'O', '.', '#'], ['#', '#', '#', '#', '#']]
# blue_x, blue_y , red_x, red_y = 3,1,1,3
from collections import deque 

q = deque()

q.append((blue_x, blue_y , red_x, red_y, 0))

# 4가지 방향
dx = [1,0,-1,0]
dy = [0,1,0,-1]


# 한방향으로 끝까지 이동해야 함 

def move(bx, by, rx, ry, dir) :

    blue_hole=False
    red_hole = False
    if dir == 0:
        if bx > rx:
            while board[by+dy[dir]][bx+dx[dir]] != "#" and (bx+dx[dir], by+dy[dir]) != (rx, ry):
                bx += dx[dir]
                if board[by][bx] == "O" :
                    blue_hole = True
                    by, bx = -1, -1 
                    break
            while board[ry+dy[dir]][rx+dx[dir]] != "#" and (rx+dx[dir], ry+dy[dir]) != (bx, by):
                rx += dx[dir]
                if board[ry][rx] == "O" :
                    red_hole = True
                    ry, rx = -1, -1
                    break
            if blue_hole == True or red_hole == True :
                return  bx, by, rx, ry, red_hole, blue_hole

        else:
            while board[ry+dy[dir]][rx+dx[dir]] != "#" and (rx+dx[dir], ry+dy[dir]) != (bx, by):
                rx += dx[dir]
                if board[ry][rx] == "O" :
                    red_hole = True
                    ry, rx = -1, -1
                    break
            while board[by+dy[dir]][bx+dx[dir]] != "#" and (bx+dx[dir], by+dy[dir]) != (rx, ry):
                bx += dx[dir]
                if board[by][bx] == "O" :
                    blue_hole = True
                    by, bx = -1, -1 
                    break
            if blue_hole == True or red_hole == True :
                return  bx, by, rx, ry, red_hole, blue_hole            

    # 아래로 기울이는 건
    if dir == 1:
        if by > ry:
            while board[by+dy[dir]][bx+dx[dir]] != "#" and (bx+dx[dir], by+dy[dir]) != (rx, ry):
                by += dy[dir]
                if board[by][bx] == "O" :
                    blue_hole = True
                    by, bx = -1, -1 
                    break
            
            while board[ry+dy[dir]][rx+dx[dir]] != "#" and (rx+dx[dir], ry+dy[dir]) != (bx, by):
                ry += dy[dir]
                if board[ry][rx] == "O" :
                    red_hole = True
                    ry, rx = -1, -1
                    break
            if blue_hole == True or red_hole == True :
                return  bx, by, rx, ry, red_hole, blue_hole            

        else:
            while board[ry+dy[dir]][rx+dx[dir]] != "#" and (rx+dx[dir], ry+dy[dir]) != (bx, by):
                ry += dy[dir]
                if board[ry][rx] == "O" :
                    red_hole = True
                    rx, ry = -1, -1
                    break        
            while board[by+dy[dir]][bx+dx[dir]] != "#" and (bx+dx[dir], by+dy[dir]) != (rx, ry):
                by += dy[dir]
                if board[by][bx] == "O" :
                    blue_hole = True
                    bx, by = -1, -1
                    break
            if blue_hole == True or red_hole == True :
                return  bx, by, rx, ry, red_hole, blue_hole            
            

    # 왼쪽으로 기울이는 건
    if dir == 2:
        if bx < rx:
            while board[by+dy[dir]][bx+dx[dir]] != "#" and (bx+dx[dir], by+dy[dir]) != (rx, ry):
                bx += dx[dir]
                if board[by][bx] == "O" :
                    blue_hole = True
                    bx, by = -1, -1
                    break            
            while board[ry+dy[dir]][rx+dx[dir]] != "#" and (rx+dx[dir], ry+dy[dir]) != (bx, by):
                rx += dx[dir]
                if board[ry][rx] == "O" :
                    red_hole = True
                    ry, rx = -1, -1
                    break    
            if blue_hole == True or red_hole == True :
                return  bx, by, rx, ry, red_hole, blue_hole            
    
        else:
            while board[ry+dy[dir]][rx+dx[dir]] != "#" and (rx+dx[dir], ry+dy[dir]) != (bx, by):
                rx += dx[dir]
                if board[ry][rx] == "O" :
                    red_hole = True
                    ry, rx = -1, -1
                    break
            while board[by+dy[dir]][bx+dx[dir]] != "#" and (bx+dx[dir], by+dy[dir]) != (rx, ry):
                bx += dx[dir]
                if board[by][bx] == "O" :
                    blue_hole = True
                    by, bx = -1,-1
                    break
                
            if blue_hole == True or red_hole == True :
                return  bx, by, rx, ry, red_hole, blue_hole            
    

    # 위로 기울이는 건
    if dir == 3:
        if by < ry:
            while board[by+dy[dir]][bx+dx[dir]] != "#" and (bx+dx[dir], by+dy[dir]) != (rx, ry):
                by += dy[dir]
                if board[by][bx] == "O" :
                    blue_hole = True
                    by, bx = -1, -1
                    break            
            while board[ry+dy[dir]][rx+dx[dir]] != "#" and (rx+dx[dir], ry+dy[dir]) != (bx, by):
                ry += dy[dir]
                if board[ry][rx] == "O" :
                    red_hole = True
                    ry, rx = -1, -1
                    break
                
            if blue_hole == True or red_hole == True :
                return  bx, by, rx, ry, red_hole, blue_hole            
        
        else:
            while board[ry+dy[dir]][rx+dx[dir]] != "#" and (rx+dx[dir], ry+dy[dir]) != (bx, by):
                ry += dy[dir]
                if board[ry][rx] == "O" :
                    red_hole = True
                    rx,ry = -1 ,-1
                    break        
            while board[by+dy[dir]][bx+dx[dir]] != "#" and (bx+dx[dir], by+dy[dir]) != (rx, ry):
                by += dy[dir]
                if board[by][bx] == "O" :
                    blue_hole = True
                    bx, by = -1,-1
                    break
            if blue_hole == True or red_hole == True :
                return  bx, by, rx, ry, red_hole, blue_hole            
        

    return bx, by, rx, ry, red_hole, blue_hole

while q :
    #기존에 있던 좌표는 bx, by...
    bx, by, rx, ry, cnt = q.popleft()
    for dir in range(4) :
        #움직일 좌표는 bbx, bby 
        bbx,bby,rrx, rry, r_h, b_h =move(bx, by, rx, ry, dir)
        # print(rry, rrx, bby, bbx)
        # print(board[rry][rrx], board[bby], board[bbx])
        # print(bbx,bby,rrx, rry, r_h, b_h)
        if r_h == True and b_h == True :
            continue
    
        if r_h == True :
            print(cnt + 1)
            exit()
        if b_h == True :
            continue
        if (bbx, bby, rrx, rry) in visited_set:
            continue
        visited_set.add((bbx, bby, rrx, rry))
        q.append((bbx, bby, rrx, rry, cnt + 1))

print(-1)
