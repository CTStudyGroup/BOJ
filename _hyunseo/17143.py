import sys

input = sys.stdin.readline

def eat_shark(k) :
    '''k라는 행 정보가 주어졌을 때, 
    열에 있는 샤크 잡아먹기'''
    for y in range(R) :
        if board[y][k] != 0 :
            # print(f'y : {y} k :{k}')
            eaten_shark= board[y][k]  # 낚시 왕이 잡은 상어에 더하기
            dic.pop(board[y][k])  # 잡아서 사라짐
            board[y][k] = 0  # 잡아서 사라짐
            return eaten_shark
        
        
def reflect_with_dir(x, size, dir, axis):
    """축(axis=0:행, 1:열) 기준으로 좌표와 방향을 반사"""
    if size == 1:
        return 0, dir  # 크기가 1이면 항상 0, 방향 변화 없음

    cycle = 2 * (size - 1)
    pos = x % cycle

    if pos < size:
        return pos, dir
    else:
        # 반사된 좌표
        new_pos = cycle - pos
        # 방향 전환
        if axis == 0:  # 행(상/하)
            new_dir = 2 if dir == 0 else 0  # 0<->2
        else:          # 열(좌/우)
            new_dir = 3 if dir == 1 else 1  # 1<->3
        return new_pos, new_dir


def move_one_shark(r, c, s, dir, z):
    d = [[1,0], [0,1], [-1,0], [0,-1]]
    tr, tc = r + s*d[dir][0], c + s*d[dir][1]
    if tr <0 or tr >= R :
        tr, dir = reflect_with_dir(tr, R, dir, axis=0)  # 행 처리
    elif tc < 0 or tc >= C:
        tc, dir = reflect_with_dir(tc, C, dir, axis=1)  # 열 처리

    return tr, tc, s, dir, z

    
    
def move_sharks() :
    new_board = [[0]*C for _ in range(R)]
    for i in range(R) :
        for j in range(C) :
            if board[i][j] != 0 :
                #상어가 있으면
                shark_num = board[i][j]
                r, c, s, d, z = dic[shark_num]
                nr, nc, s, nd, z = move_one_shark(r, c, s, d, z)
                if new_board[nr][nc] == 0 :
                    new_board[nr][nc] = z
                    dic[shark_num] = [nr, nc, s, nd, z]
                elif new_board[nr][nc] > shark_num :
                    dic.pop(shark_num)
                else :
                    tmp_shark = new_board[nr][nc]
                    dic.pop(tmp_shark)
                    new_board[nr][nc] = shark_num
                    dic[shark_num] = [nr, nc, s, nd, z]
    return new_board
def solve() :
    global board
    king = -1
    answer = 0
    while king < C - 1:
        # print("before ")
        # for b in board :
        #     print(b)
        # print("--------------")

        king += 1  # 왕 이동
        tmp = eat_shark(king)
        if tmp :
            answer += tmp
        # print(f'king : {king} tmp : {tmp}')
        
        board = move_sharks()
    #     print("after")
    #     for b in board :
    #         print(b)
    #     print(dic)
    #     print("----------------------------")
    print(answer)
    sys.exit()

R, C, M = map(int, input().split())
if M == 0 :
    print(0)
    sys.exit()
    
dic = {}
board = [[0]*C for _ in range(R)]
for _ in range(M) :
    r, c, s, td, z = map(int, input().split())
    r -= 1  # 0-based index
    c -= 1  # 0-based index
    if td == 1 :
        d = 2
    elif td == 2 :
        d = 0
    elif td == 3 :
        d = 1
    elif td == 4 :
        d = 3
    dic[z] = [r, c, s, d, z]
    board[r][c] = z

solve()
                
