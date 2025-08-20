'''
크기가 N * N 인 체스판
흰색, 빨간색, 파란색 칸임 

말의 개수는 K
말은 원판 모양 -> 쌓기 가능
1~ K까지 번호 있음
이동 방향은 미리 정해져 있음 (위, 아래, 왼, 오)

시작 : 말 K개를 놓고

턴 1 : 1부터 K까지 이동
위에 올려져 있는 말도 함께 이동

종료 : 말이 4개 이상 쌓이면 종료

'''
import sys

d = [[-100, 100], [0, 1], [0, -1], [-1, 0], [1, 0]]


def blue_move(y, x, dir, num, below, upper,turn) :
    global horses
    # 반대 방향 조회
    if dir % 2 == 1 :
        dir += 1
    else : 
        dir -= 1
    horses[num] = dir
    ny, nx = y + d[dir][0], x + d[dir][1] 
    if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] == 2 :

        return
    
    else :
        if board[ny][nx] == 0:        
            horses_board[y][x] = below  # 아래는 두고
            horses_board[ny][nx] += upper
            for new in upper :  # loc 갱신
                loc[new] = [ny, nx]
        if board[ny][nx] == 1 :
            horses_board[y][x] = below
            horses_board[ny][nx]+= upper[::-1]
            for new in upper :  # loc 갱신
                loc[new] = [ny, nx]
    if len(horses_board[ny][nx]) >= 4: print(turn); sys.exit()
    
    

def move(y, x, dir, num, turn) :
    ny, nx = y + d[dir][0], x + d[dir][1]
    tmp = horses_board[y][x]  # 현재 좌표의 말 배열
    tmp_idx = tmp.index(num)  # 현재 말의 위치 (위에만 이동시켜야 함)

    
    below = tmp[:tmp_idx]
    upper = tmp[tmp_idx :]
    if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] == 2 :
        blue_move(y, x, dir, num, below, upper, turn)
    elif board[ny][nx] == 0 :  # 이동하려는 좌표가 흰색
        horses_board[y][x] = below  # 아래는 두고
        horses_board[ny][nx] += upper
        
        for new in upper :  # loc 갱신
            loc[new] = [ny, nx]
        if len(horses_board[ny][nx]) >= 4: print(turn); sys.exit()

    elif board[ny][nx] == 1 :  # 이동하려는 좌표가 빨간색
        horses_board[y][x] = below
        horses_board[ny][nx]+= upper[::-1]
        
        for new in upper :  # loc 갱신
            loc[new] = [ny, nx]
            
        if len(horses_board[ny][nx]) >= 4: print(turn); sys.exit()
            
            
    

def solve() :
    turn =1
    while turn <= 1000 :
        
        # 1~ K 말 이동 
        for num in range(1, K+1) :
            y, x = loc[num]  # 현재 위치
            dir = horses[num]  #  말 진행 방향
            move(y, x, dir, num, turn)
        turn += 1
    print(-1)
        

# 입력
N, K = map(int, input().split())  # 체스판 N 말 개수 K
board = [list(map(int, input().split())) for _ in range(N)]  # 보드 자체
horses_board = [[[] for _ in range(N)] for _ in range(N)]

horses = [-1]
loc = [[-1,-1]]
for number in range(1, K + 1) :
    y, x, dir = map(int, input().split())
    y, x = y-1, x-1
    horses_board[y][x].append(number)
    horses.append(dir)
    loc.append([y,x])
# horses[idx] = 방향 idx번(1번부터 시작)의 방향은 1,2,3,4
# 1은 오른쪽, 2은 왼쪽, 3은 위, 4은 아래

# horses_board는 y, x 좌표에 있는 목록

# board는 next 참고용으로 (0, 1, 2)
# 0이 흰색, 1이 빨간색, 2는 파란색

# loc[idx] = [y, x] idx(1부터 시작) 번 말의 현재 위치
solve()
