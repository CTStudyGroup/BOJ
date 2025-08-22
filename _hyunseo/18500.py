import sys
from collections import defaultdict, deque

input  = sys.stdin.readline
d = [[1,0], [-1,0], [0,-1], [0,1]]


def attack(turn, height) :
    '''공격해서 사라진 미네랄 좌표 반환 
    없으면 -1 반환 '''
    line = board[height]
    if 'x' not in line :  # 만약 파괴할 미네랄이 없는 경우
        return -1, -1
    if turn == 0 :
        idx = line.index('x')
        
    else :
        idx = line[::-1].index('x')
        idx = C-idx-1
    board[height][idx] = '.'
    return height, idx


def get_cluster(y, x) :
    '''클러스터 반환, '''
    q = deque()
    q.append((y,x))
    visited = set()
    visited.add((y, x))
    while q :
        y, x = q.popleft()
        for dir in range(4) :
            ty, tx = y + d[dir][0],  x + d[dir][1]
            if ty < 0 or ty >= R or tx < 0 or tx >= C : continue
            if board[ty][tx] == 'x' and (ty,tx) not in visited:
                q.append((ty, tx))
                visited.add((ty, tx))
    if not visited :
        return True
    flag = False  # 떠있는지의 여부, 떠있으면 False
    for y, x in visited :
        if y == R-1 :
            flag = True
            break
        for dir in range(4) :
            ty, tx = y + d[dir][0],  x + d[dir][1]
            if ty < 0 or ty >= R or tx < 0 or tx >= C or (ty, tx) in visited : continue
            if board[ty][tx] == 'x' :
                flag = True 
                break
    return flag, visited

def drop_cluster(cluster):
    dif = sys.maxsize

    for y, x in cluster:
        step = 0
        ny = y + 1
        while ny < R:
            if board[ny][x] == 'x' and (ny, x) not in cluster:
                break
            ny += 1
            step += 1
        dif = min(dif, step)
    for c in cluster :
        y, x = c
        board[y][x] = '.'
    for c in cluster :
        y, x = c
        board[y + dif][x] = 'x'

R, C = map(int, input().split())
board = []
for _ in range(R) :
    board.append(list(input().strip()))
N = int(input())
attack_height = list(map(int, input().split()))

for i in range(N) :
    y, x = attack(i%2, R -  attack_height[i] )
    if y == -1 or x == -1 : continue
    for dir in range(4) :
        ny, nx = y + d[dir][0], x + d[dir][1]
        if ny < 0 or ny >= R or nx < 0 or nx >= C : continue
        if board[ny][nx] == 'x':
            flag, cluster = get_cluster(ny, nx)
            if not flag :
                drop_cluster(cluster)
            
for line in board :
    print(''.join(line))
