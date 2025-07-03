from collections import deque


def find_biggest_group(board):
    groups = []
    visited_all = [[False]*N for _ in range(N)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def dfs(x, y, normal_color, visited, tmp):
        visited[y][x] = True
        tmp.append((y,x))
        
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx]:
                    block = board[ny][nx]
                    if block == 0:
                        dfs(nx, ny, normal_color, visited, tmp)
                    elif block == normal_color:
                        dfs(nx, ny, normal_color, visited, tmp)
    
    for y in range(N):
        for x in range(N):
            if board[y][x] =='' :
                continue
            if board[y][x] > 0 and not visited_all[y][x]:
                visited = [[False]*N for _ in range(N)]
                tmp = []
                dfs(x, y, board[y][x], visited, tmp)
                
                # visited한 칸은 visited_all에도 표시
                for ty in range(N):
                    for tx in range(N):
                        if visited[ty][tx] and board[ty][tx] != 0:
                            visited_all[ty][tx] = True

                if len(tmp) > 0:
                    rainbow_cnt = sum(1 for (yy, xx) in tmp if board[yy][xx] == 0)
                    standard_blocks = [pos for pos in tmp if board[pos[0]][pos[1]] != 0]
                    if standard_blocks:
                        standard_block = min(standard_blocks)
                        groups.append((len(tmp), rainbow_cnt, standard_block ,tmp) )

    # 가장 큰 그룹 찾기
    if groups:
        groups.sort(
    key=lambda x: (-x[0], -x[1], -x[2][0], -x[2][1])
)
        return groups[0][3]
    else :
        return []
def erase(board, group, score) :
    # print("---", group)
    score += len(group)**2
    for y,x in group :
        board[y][x] = ''
    return board, score

def gravity(board) :
    #검은색 블록을 제외한 모든 블록이 이동
    for j in range(N) :
        blocks_to_fall = deque()
        base = N-1
        for i in range(N-1, -1, -1) :
            if board[i][j] == '' :
                continue;
            elif board[i][j] == -1:
                if blocks_to_fall :
                    for b in range(base, base-len(blocks_to_fall), -1) :
                        board[b][j] = (blocks_to_fall.popleft())
                blocks_to_fall = deque()
                base = i-1
            else :
                blocks_to_fall.append(board[i][j])
                board[i][j] = ''
        if blocks_to_fall :
            for b in range(base, base-len(blocks_to_fall), -1) :
                board[b][j] = (blocks_to_fall.popleft())
                
    return board     

def spin(board) :
    new_board = [[0]*N for _ in range(N)]
    x = 0
    for line in board :
        for idx, val in enumerate(line) :
            new_board[abs(N-1-idx)][x] = val
        x += 1
    board = new_board
    return board

def check_end(board) :
    # 게임이 끝났을 경우 True
    for i in range(len(board)) : 
        for j in range(len(board[0])) :
            if board[i][j] == '' or board[i][j] == -1 :
                continue
            else:
                return False
    return True

score = 0
N, M = map(int, input().split())
board = []
for n in range(N) :
    board.append(list(map(int, input().split())))
while check_end(board) is False :
    # print("\n------------")
    # for i in board :
    #     print(i)
    # print(score)
    erase_group = find_biggest_group(board)
    if len(erase_group) <= 1 :
        break
    board, score = erase(board, erase_group, score)
    board = gravity(board)
    board = spin(board)
    board = gravity(board)

print(score)
