import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
PP, PC = map(int, input().split())

dir_map = {
    "\\": [3, 2, 1, 0],
    "/": [1, 0, 3, 2]
}

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 칸마다 방문했던 방향 저장하기
# 이미 방문한 칸 && 방문했던 방향이면 거기서부턴 무한 전파 가능
def move(sy, sx, sd):
    cy, cx, d = sy, sx, sd
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    ret = 0

    while True:
        # print("cy:", cy, ", cx:", cx, ", d:", d)
        if visited[cy][cx][d]:
            return -1  # 무한 전파 가능

        visited[cy][cx][d] = True

        if matrix[cy][cx] == "C":  # 블랙홀
            return ret

        if matrix[cy][cx] != ".":  # 방향 전환
            d = dir_map[matrix[ny][nx]][d]
            # print("방향 전환 to ", d)

        ny = cy + dy[d]
        nx = cx + dx[d]
        ret += 1

        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            return ret

        cy, cx = ny, nx

dString = {0: "U", 1: "R", 2: "D", 3: "L"}
ans_dir = -1
ans_dist = -1
for i in range(4):
    dist = move(PP - 1, PC - 1, i)
    if dist == -1:
        print(dString[i])
        print("Voyager")
        exit()
    else:
        if dist > ans_dist:
            ans_dist = dist
            ans_dir = i

print(dString[ans_dir])
print(ans_dist)
