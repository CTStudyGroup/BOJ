import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 입력 받기
R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]

visited = [False] * 26

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

# 최대 이동 거리
max_depth = 0

# 방문 상태 저장
visited_states = set()


def dfs(y, x, depth):
    global matrix, visited, max_depth, R, C
    # print("dfs called:", y, x, depth)

    max_depth = max(max_depth, depth)

    # 현재 상태를 저장
    state = (y, x, tuple(visited))
    if state in visited_states:
        return
    visited_states.add(state)

    # 다음 노드 방문
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            char_index = ord(matrix[ny][nx]) - 65

            # 알파벳 중복 확인
            if not visited[char_index]:
                visited[char_index] = True
                dfs(ny, nx, depth + 1)
                visited[char_index] = False


visited[ord(matrix[0][0]) - 65] = True
dfs(0, 0, 1)

print(max_depth)
