'''공격하는 적은 D이하인 적 중 가장 가까운 적, 왼쪽에 있는 적

같은 적이 여러 궁수에게 공격 가능
공격 받으면 사라짐

궁수의 공격이 끝나면 -> 적 이동

적은 아래로 한칸, 성이 있는 칸으로 이동하면 게임에서 제외
모든 적이 사라지면 게임 끗

구하는 것 : 궁수의 공격으로 제거할 수 있는 최대 수 적 

두 점 사이의 거리는 abs(y1 - y2) + abs(x1 + x2)
'''

# print(board)
from collections import deque

# N, M, D = 5, 5, 2
# board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],  [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]  

def attack_one(a) :
    q = deque()
    q.append((N-1, a, 1))  # 제일 가까운 좌표 입력
    d = [[0, -1], [-1, 0], [0,1]]
    while q :
        y, x, cnt = q.popleft()
        if cnt > D : continue
        if board[y][x] == 1 :
            return ( y, x)  # 
        for dir in range(3) :
            ty, tx = y + d[dir][0], x + d[dir][1]
            if ty <0 or ty >= N or tx < 0 or tx >= M : continue
            
            q.append((ty, tx, cnt + 1))
            
    return (-1,-1 )#만약 없는 경우에는 -1 반환
def attack(a, b, c) :
    attacked = set()
    attacked.add(attack_one(a))
    attacked.add(attack_one(b))
    attacked.add(attack_one(c))
    if (-1, -1) in attacked : 
        attacked.remove((-1, -1))
    for y, x in attacked :
        board[y][x] = 0  # 적 없애기
    return len(attacked)  # 없앤 적 수 반환

def move() :
    global board
    new_board = [[0]*M for _ in range(N)]
    for i in range(N-2, -1, -1) :  # 마지막 줄 제외
        for j in range(M) :
            if board[i][j] == 1 :
                new_board[i+1][j] = 1
    removed = 0
    for j in range(M) :
        if board[N-1][j] == 1 :
            removed += 1
    board = new_board
    return removed

def solve(lst ):
    a, b, c = lst
    removed_enemy = 0
    answer = 0
    cnt = 0
    while removed_enemy != total_enemy:
        tmp = attack(a, b, c)
        removed_enemy += tmp
        answer += tmp
        removed_enemy += move()
        for line in board :
            print(line)
        cnt += 1
    print("---------------")
    return answer

N, M, D = map(int, input().split())
base_board = []
for _ in range(N) :
    base_board.append(list(map(int, input().split())))
total_enemy = sum([1 for line in base_board for t in line if t == 1])

max_answer = 0


from itertools import combinations

possible_arrows = list(combinations([i for i in range(M)], 3))
for arrows in possible_arrows :
    if max_answer == total_enemy :
        print(max_answer)
        exit()
    board = [row[:] for row in base_board]
    max_answer = max(max_answer, solve( arrows))
print(max_answer)
