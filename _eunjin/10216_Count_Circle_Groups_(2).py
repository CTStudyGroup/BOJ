from collections import deque
import sys
input = sys.stdin.readline

# 특정 원 -> 다른 모든 원에 대해 통신 거리 안에 있는지 여부 파악
def valid(curr, target):
    cy, cx, cr = circles[curr]
    ty, tx, tr = circles[target]

    return (cy - ty)**2 + (cx - tx)**2 <= (cr + tr)**2

def bfs(s):
    q = deque()
    q.append(s)  # 원의 인덱스
    visited[s] = True

    while q:
        circle = q.popleft()

        for i in range(N):
            if i == circle:  # 자기 자신은 pass
                continue

            if not visited[i] and valid(circle, i):
                q.append(i)
                visited[i] = True

T = int(input())

for _ in range(T):
    N = int(input())
    circles = []
    answer = 0

    for _ in range(N):
        circles.append(list(map(int, input().split())))

    visited = [False] * N

    for i in range(N):
        if not visited[i]:
            bfs(i)
            answer += 1

    print(answer)

