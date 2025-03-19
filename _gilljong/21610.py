from sys import stdin as s

s = open("txt/21610.txt", "r")

# 격자 크기 1씩 패딩
# 현재 위치 % 격자 크기로 이동
# 비바라기 시전 시 좌측 하단 비구름 생성 [5,1][5,2][4,1][4,2] 여기서 위로 4칸 ?
# 비구름 이동, 비구름 좌표 이동, 이동 후 해당 그리드 값 +1
# 비구름 좌표를 기준으로 물복사버그 함수 작성 후 해당 그리드 값 + n
# 구름 칸을 제외하고, 나머지 칸에서 물의 양 2이상인 칸은 -2씩 빼기, 구름 위치 get

N, M = map(int, s.readline().split())

grid = [list(map(int, s.readline().split())) for _ in range(N)]

directions = [list(map(int, s.readline().split())) for _ in range(M)] # [방향, 거리]

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)] # 초기 구름 위치 지정

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

def water_bug(x,y): # 대각선 위치의 물 확인
    cnt = 0
    if x-1 >= 0 and y - 1 >= 0 and grid[x-1][y-1] > 0:
        cnt += 1
    if x-1 >= 0 and y + 1 < N and grid[x-1][y+1] > 0:
        cnt += 1
    if x+1 < N and y - 1 >= 0 and grid[x+1][y-1] > 0:
        cnt += 1
    if x+1 < N and y + 1 < N and grid[x+1][y+1] > 0:
        cnt += 1
    return cnt

for d,s in directions: # M번 이동
    for i in range(len(cloud)): # 구름 이동
        nx = (cloud[i][0] + dx[d-1]*s) % N # 다음 구름 좌표
        ny = (cloud[i][1] + dy[d-1]*s) % N
        cloud[i] = (nx,ny)

    visited = [[0] * N for _ in range(N)] # 구름 위치

    for i in range(len(cloud)): #구름 물의 양 +1
        grid[cloud[i][0]][cloud[i][1]] += 1
        visited[cloud[i][0]][cloud[i][1]] = 1 # 구름의 위치 체크

    for i in range(len(cloud)): # 물복사버그
        grid[cloud[i][0]][cloud[i][1]] += + water_bug(cloud[i][0],cloud[i][1])

    cloud = [] # 새로운 구름 받기

    for i in range(N): # 새로운 구름 처리
        for j in range(N):
            if visited[i][j] == 0 and grid[i][j] >= 2:
                grid[i][j] -= 2
                cloud.append([i,j])

result = 0
for i in range(N):
    for j in range(N):
        result += grid[i][j]

print(result)