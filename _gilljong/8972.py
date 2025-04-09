from sys import stdin as s
from collections import defaultdict
s = open('txt/8972.txt', 'r')

R, C = map(int, s.readline().split())

grid = [ list(s.readline().strip()) for _ in range(R) ]
visited = [[0] * R for _ in range(C)]

d = list(map(int, s.readline().strip()))

directions = [[1,-1],[1,0],[1,1],[0,-1],[0,0],[0,1],[-1,-1], [-1,0], [-1,1]]

t = 0 # 시간
aduino = []
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'I':
            jongsu = [i,j]
        elif grid[i][j] == 'R':
            aduino.append((i,j))

aduino_numbers = len(aduino)

def follow(robot, aduino):
    distance = 999
    last_direction = 0
    for i in range(9):
        nx, ny = aduino[0] + directions[i][0], aduino[1] + directions[i][1]

        new_distance = abs(robot[0] - nx) + abs(robot[1] - ny)
        if distance > new_distance:
            distance = new_distance
            last_direction = i

    #print(last_direction)
    return last_direction

for idx, item in enumerate(d):
    pass
    # 종수 이동
    nx = jongsu[0] + directions[item-1][0]
    ny = jongsu[1] + directions[item-1][1]
    grid[jongsu[0]][jongsu[1]] = '.'
    jongsu = [nx,ny]
    grid[nx][ny] = 'I'
    pass
    # 미친아두이노 이동
    k = defaultdict(int)

    for idx_d, crazy in enumerate(aduino):
        x,y = crazy
        current_d = follow(jongsu, (x,y))
        ax = x+directions[current_d][0]
        ay = y+directions[current_d][1]
        aduino[idx_d] = (ax, ay)

        # 종수, 아두이노
        if [ax,ay] == [nx, ny]:
            print("kraj",idx+1)
            exit()

        k[str(ax)+','+str(ay)] += 1
        pass
    for key in k:
        if k[key] > 1:
            cx, cy = map(int,key.split(','))
            for _ in range(k[key]):
                aduino.remove((cx,cy))
            grid[cx][cy] = '.'

for i in range(R):
    for j in range(C):
        if grid[i][j] != 'I':
            grid[i][j] = '.'

for x,y in aduino:
    grid[x][y] = 'R'

for i in range(R):
    for j in range(C):
        print(grid[i][j], end='')
    print()
