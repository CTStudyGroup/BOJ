# 1-index임
# 처음에는 모든 칸에 5난큼의 양분이 있음

# M개의 나무를 구매 -> 땅 심음
# 한 칸에 여러개의 나무 심을 수 있음

# 봄에는 나이만큼 양분 먹고, 나이 +1
# 하나의 칸에 여러개의 나무가 있으면 어린 나무부터
# 양분을 먹고
# 만약 양분이 없어서, 나이만큼 못 먹으면 즉시 죽음

# 여름에는 죽은 나무가 양분으로 변함
# 죽은 나무 나이를 2로 나눈 값이 양분으로 추가 (x 소수점)

# 가을에는 번식
# 나무의 나이가 5의 배수, 인접한 8개의 칸에 나이가 1인 나무
# 주변 3*3 (범위 내에섬ㄴ)

# 겨울에는 A만큼 양분이 추가함

# K 년 후 나무의 개수
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = []
for _ in range(N) :
    A.append(list(map(int, input().split())) )

import heapq
from collections import deque

# 나무 나이
grid = [[deque() for _ in range(N)] for _ in range(N)]


# 나무 나이 관리 q
q = []
for _ in range(M) :
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1  # 0- index로 맞추기
    grid[x][y].append(z)
    heapq.heappush(q, [z, y, x])
    
# 재정렬
for i in range(N):
    for j in range(N):
        grid[i][j] = deque(sorted(grid[i][j]))
# nutrition이 양분 
nutrition = [[5]*N for _ in range(N)]
def one_year() :
    dead_tree = deque()
    # 봄
    
    for y in range(N) :
        for x in range(N) :
            length = len(grid[y][x])
            dead_nutrition = 0
            for _ in range(length) :
                age = grid[y][x].popleft()
                # 양분을 먹지 못하는 경우
                if age > nutrition[y][x] :
                    dead_nutrition += (age//2)
                else : # 양분을 먹을 수 있는 경우
                    nutrition[y][x] -= (age)
                    grid[y][x].append(age + 1)
            nutrition[y][x] += dead_nutrition

    
    d = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1],[1,-1],[1,0],[1,1]]
    # 가을
    
    for y in range(N) :
        for x in range(N ) :
            for tree_age in grid[y][x] :
                if tree_age % 5 == 0 :
                    for dir in range(8 ):
                        ty, tx = y + d[dir][0] , x + d[dir][1]
                        if 0<=ty<N and 0<=tx<N :
                            grid[ty][tx].appendleft(1)
            nutrition[y][x] += A[y][x]

    
for year in range(K) :
    one_year()
    

answer = 0 
for y in range(N) :
    for x in range(N) :
        answer += len(grid[y][x])         

print(answer)
