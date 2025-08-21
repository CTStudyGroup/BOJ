import sys
input = sys.stdin.readline

# 방향: 상(1), 하(2), 좌(3), 우(4)
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
center = [N//2, N//2]

commands = list(map(int, input().split())) for _ in range(M))

def attack(dir, s):
    '''마법사 공격'''
    global board
    for dist in range(1, s + 1):
        ny, nx = center[0] + dy[dir]*dist, center[1] + dx[dir]*dist
        if 0 <= ny < N and 0 <= nx < N:
            board[ny][nx] = 0

def stringify(board):
    '''달팽이 모양으로 1차원 배열 변환'''
    line = []
    d = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 좌, 하, 우, 상
    y, x = N//2, N//2
    turn = 0
    while len(line) < N**2:
        for _ in range(turn//2 + 1):
            y, x = y + d[turn % 4][0], x + d[turn % 4][1]
            if not (0 <= y < N and 0 <= x < N):
                return line[:-1]
            line.append(board[y][x])
        turn += 1
    return line[:-1]

def pull(line):
    '''빈칸(0) 없애고 땡기기'''
    return [l for l in line if l != 0]

def explode(line):
    '''4개 이상 연속 구슬 폭발'''
    flag = False
    new_line = []
    idx = 0
    score = 0
    while idx < len(line):
        j = idx
        while j < len(line) and line[j] == line[idx]:
            j += 1
        if j - idx >= 4:  # 폭발
            flag = True
            score += line[idx] * (j - idx)
        else:
            new_line.extend(line[idx:j])
        idx = j
    return flag, new_line, score

def transform(line):
    '''구슬을 (개수, 숫자) 형태로 변환'''
    new_line = []
    idx = 0
    while idx < len(line):
        j = idx
        while j < len(line) and line[j] == line[idx]:
            j += 1
        new_line.append(j - idx)
        new_line.append(line[idx])
        idx = j
        if len(new_line) >= N**2 - 1:
            break
    return new_line[:N**2-1]

def boardify(line):
    '''1차원 배열을 다시 달팽이 모양 보드로'''
    new_board = [[0]*N for _ in range(N)]
    d = [[0,-1],[1,0],[0,1],[-1,0]]
    y, x = N//2, N//2
    turn = 0
    idx = 0
    while idx < len(line) and idx < N**2-1:
        for _ in range(turn//2 + 1):
            y, x = y + d[turn % 4][0], x + d[turn % 4][1]
            if not (0 <= y < N and 0 <= x < N): 
                return new_board
            new_board[y][x] = line[idx]
            idx += 1
        turn += 1
    return new_board

def one_strike(dir, s):
    global board
    # 공격
    attack(dir, s)
    # stringify
    line = stringify(board)
    # 구슬 이동
    line = pull(line)
    total_score = 0
    # 구슬 폭발 반복
    while True:
        flag, line, score = explode(line)
        total_score += score
        if not flag:
            break
        line = pull(line)
    # 그룹 변환
    line = transform(line)
    # 다시 보드화
    board = boardify(line)
    return total_score

# ===== 실행 =====
answer = 0
for dir, s in commands:
    answer += one_strike(dir, s)

print(answer)
