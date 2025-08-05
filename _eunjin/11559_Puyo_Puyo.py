from collections import deque
import copy
matrix = [list(input()) for _ in range(12)]
H = 12
W = 6
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

# 중력 작용: 바닥 or 다른 블록 나올 때까지 아래로 내리기
# 연쇄 작용: 같은 색 노드가 4개이상 인접하면 해당 블록 제거. = 이게 1 연쇄
#  -제거해야할 연결 요소가 여러개면 동시에 제거하고, 여러개 연결요소가 제거되더라도 1 연쇄로 카운트
# 블록 제거 후 다시 중력 작용
# 중력 작용한 후 다시 연쇄 작용

def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()

# 중력 작용, 이동 발생 했으면 True, 발생 안했으면 False 리턴
def gravity():
    ret = False

    # 아래서부터 확인하면서 자신의 아래칸이 .이면 계속 내리기
    for y in range(10, -1, -1):
        for x in range(6):
            if matrix[y][x] == ".":
                continue

            curr = matrix[y][x]

            ny = y
            while ny < H - 1:
                ny += 1
                if matrix[ny][x] != ".":
                    ny -= 1
                    break

            if ny != y:  # 이동시켜야 하는 경우
                matrix[ny][x] = matrix[y][x]
                matrix[y][x] = "."
                ret = True
    return ret

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True
    ret = []

    while q:
        cy, cx = q.popleft()
        ret.append((cy, cx))

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue

            if not visited[ny][nx] and matrix[ny][nx] == matrix[cy][cx]:
                q.append((ny, nx))
                visited[ny][nx] = True
    return ret


# 연쇄 작용, 연쇄 발생했으면 True, 안했으면 False 리턴
# bfs로 연결 요소 탐색, 개수가 4 이상이면 해당 노드들 모두 제거 후보에 추가
# 모든 bfs 탐색 후 노드 제거 후보 제거
def explode():
    ret = False
    explode_nodes = []
    for y in range(11, -1, -1):
        for x in range(6):
            if matrix[y][x] == "." or visited[y][x]:
                continue

            nodes = bfs(y, x)
            if len(nodes) >= 4:
                explode_nodes.extend(nodes)

    # print("explode_nodes:", explode_nodes)
    if explode_nodes:
        ret = True

    for y, x in explode_nodes:
        matrix[y][x] = "."

    return ret


answer = 0

while True:
    grav = gravity()
    visited = [[False] * W for _ in range(H)]
    exp = explode()

    if not exp:
        break
    else:
        answer += 1

print(answer)

