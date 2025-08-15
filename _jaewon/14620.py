# 백트래킹
# 최대 깊이 64라서 충분할 듯
import math

N = int(input())
matrix = []
for row in range(N):
    matrix.append(list(map(int,input().split())))   

visited = [[0 for _ in range(N)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

seed_matrix = [] # 씨앗의 좌표
minimum = float('inf')

def getPrice(centerX, centerY):
    total = 0
    total += matrix[centerY][centerX]

    for dir in range(4):
        nx = centerX + dx[dir]
        ny = centerY + dy[dir]

        total += matrix[ny][nx]
    
    return total

def backtrack(centerX, centerY, seed, total): # seed는 씨앗의 남은 개수
    global minimum
    if(seed == 0):
        minimum = min(minimum, total)
        return
    if(centerY >= N-1):  # 탐색 범위를 벗어나면 종료
        return
    
    # 이 위치에 놓으면 겹치는 경우
    # 기존 seed_matrix와 위치가 1차이 나는 경우 겹침
    available = 1
    for seedX, seedY in seed_matrix:
        distance = (centerX - seedX)**2 + (centerY - seedY)**2

        if (distance < 5):  
            available = 0
            # print(f'{centerX},{centerY}에는 놓을 수 없음')
            break
    
    # 놓을 수 있는 경우
    if(available):
        seed -= 1
        seed_matrix.append([centerX, centerY])
        price = getPrice(centerX, centerY)
        total += price

        # print(f'{centerX}, {centerY}에 놓기, 남은 씨앗: {seed}, 현재 토탈: {total}')
        if(centerX == N-2):
            backtrack(1, centerY + 1, seed, total)
        else:
            backtrack(centerX + 1, centerY, seed, total)
        
        seed += 1
        seed_matrix.pop(-1)
        total -= price

    # 안놓고 가는 경우 or 놓을 수 없는 경우
    if(centerX == N-2):
        backtrack(1, centerY + 1, seed, total)
    else:
        backtrack(centerX + 1, centerY, seed, total)

backtrack(1, 1, 3, 0)
print(minimum)


