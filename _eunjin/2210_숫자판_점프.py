matrix = [list(input().split()) for _ in range(5)]

# dfs로 이동하면서 depth가 5되면 종료
# set에 담기

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

answer = set()

def dfs(y, x, string):
    if len(string) == 6:
        answer.add(string)
        return

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
            new = string + matrix[ny][nx]
            dfs(ny, nx, new)


for y in range(5):
    for x in range(5):
        dfs(y, x, matrix[y][x])


print(len(answer))
