from sys import stdin as s
from itertools import permutations
from copy import deepcopy
s = open("txt/17406.txt", "r")

N,M,K = map(int,s.readline().split())

grid = [[0] * (M+1)]

for _ in range(N):
    grid.append([0] + list(map(int, s.readline().split())))

turn = [list(map(int, s.readline().split())) for _ in range(K)]

min_value = 999999
def trun_grid(new_grid, order): # 회전 + 배열 최솟 값 구하기
    global min_value
    for k in range(len(order)): # 순열 !
        tmp_grid = deepcopy(new_grid)

        start = (order[k][0] - order[k][2], order[k][1] - order[k][2])
        end = (order[k][0] + order[k][2], order[k][1] + order[k][2])

        size = end[0] - start[0] + 1

        for i in range(size,1,-2):
            for j in range(1, i):
                new_grid[start[0] + j - 1][start[1]] = tmp_grid[start[0] + j][start[1]]
                new_grid[start[0]][start[1]+j] = tmp_grid[start[0]][start[1]+j-1]
                new_grid[start[0]+j][start[1]+i-1] = tmp_grid[start[0] + j -1][start[1]+i-1]
                new_grid[start[0]+i-1][start[1]+j-1] = tmp_grid[start[0] + i - 1][start[1]+j]
            start = (start[0] + 1, start[1] + 1)

    for i in range(1,N+1): # 최솟 값 계산
        min_value = min(min_value,sum(new_grid[i]))

for q in permutations(turn):
    new_grid = deepcopy(grid)
    trun_grid(new_grid, q)

print(min_value)

# 57m 27s