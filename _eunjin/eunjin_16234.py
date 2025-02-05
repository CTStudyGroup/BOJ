from collections import deque

N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def get_union():  # 연함을 이루는 칸의 좌표 리스트
    global matrix
    ret = []

    visited = [[False]*N for _ in range(N)]
    q = deque()
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            # print("new start node:", r, c)

            union = [(r, c)]
            q.append((r, c))  # y,x
            visited[r][c] = True

            while(q):
                y, x = q.popleft()

                for i in range(4):
                    ny = y+dy[i]
                    nx = x+dx[i]

                    if ny < 0 or ny >= N or nx < 0 or nx >= N:
                        continue
                    if visited[ny][nx]:
                        continue
                    if L <= abs(matrix[y][x]-matrix[ny][nx]) <= R:
                        visited[ny][nx] = True
                        q.append((ny, nx))
                        union.append((ny, nx))

            if len(union) > 1:
                ret.append(union)
    return ret


T = 0
while(True):
    unions = get_union()
    if not unions:  # 연합이 없는 경우
        break
    # 인구 이동 후의 인구 수 구하기
    new_nums = []
    for union in unions:
        num = 0
        for node in union:
            num += matrix[node[0]][node[1]]
        new_nums.append(num//len(union))

    # matrix 업데이트
    for i in range(len(unions)):
        for node in unions[i]:
            matrix[node[0]][node[1]] = new_nums[i]

    T += 1


print(T)
