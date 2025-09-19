import copy
import sys
from collections import deque

sys.setrecursionlimit(10**2)
input = sys.stdin.readline

N = int(input())
grid = []
for _ in range(N) :
    grid.append(list(map(int,input().split())))
    
    
def get_max(grid) :
    '''판에서 제일 큰 수 구하기'''
    ans = 0
    for i in range(N) :
        ans = max(ans, max(grid[i]))
    return ans

def merge_line(line):
    # 0 제거
    line = [x for x in line if x != 0]
    new_line = []
    skip = False
    for i in range(len(line)):
        if skip:
            skip = False
            continue
        if i + 1 < len(line) and line[i] == line[i+1]:
            new_line.append(line[i] * 2)
            skip = True
        else:
            new_line.append(line[i])
    # 빈 칸 채우기
    while len(new_line) < N:
        new_line.append(0)
    return new_line

def move_left(grid):
    new_grid = []
    for i in range(N):
        new_grid.append(merge_line(grid[i]))
    return new_grid
def move_right(grid):
    new_grid = []
    for i in range(N):
        row = grid[i][::-1]                
        merged = merge_line(row)
        new_grid.append(merged[::-1])     
    return new_grid
def move_up(grid):
    new_grid = [[0]*N for _ in range(N)]
    for j in range(N):
        col = [grid[i][j] for i in range(N)]
        merged = merge_line(col)
        for i in range(N):
            new_grid[i][j] = merged[i]
    return new_grid
def move_down(grid):
    new_grid = [[0]*N for _ in range(N)]
    for j in range(N):
        col = [grid[i][j] for i in range(N)][::-1]  
        merged = merge_line(col)
        merged = merged[::-1]
        for i in range(N):
            new_grid[i][j] = merged[i]
    return new_grid



def move(grid, dir) :
    ''' up 0, right 1 , down 2 , left 3'''
    if dir == 0 :
        return move_up(grid)
        
    if dir == 1 :
        return move_right(grid)
        
    if dir == 2 :
        return move_down(grid)
        
    if dir == 3 :
        return move_left(grid)
        
        
def dfs(cnt, grid) :
    ''' up 0, right 1 , down 2 , left 3'''
    if cnt == 5 :
        global answer
        answer = max(answer, get_max(grid))
        return
    for dir in range(4) :
        tmp = move(copy.deepcopy(grid), dir)
        dfs(cnt+1, tmp)

answer = 0
dfs(0, grid)
print( answer)
