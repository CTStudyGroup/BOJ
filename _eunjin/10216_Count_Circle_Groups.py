import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
# 연결 요소의 개수 세기

# curr의 원 반경 안에 target이 포함되는지 여부
def valid(curr, target):
    cy, cx, cr = circles[curr]
    ty, tx, tr = circles[target]

    return (cy - ty)**2 + (cx - tx)**2 <= (cr + tr)**2

# bfs로 주어진 R거리 안에 있는 원을 대상으로 큐에 넣기
def bfs(c):
    q = deque()
    q.append(c)

    while q:
        curr = q.popleft()

        for i in range(N):
            if curr == i:
                continue

            if not visited[i] and valid(curr, i):
                q.append(i)
                visited[i] = True


for _ in range(T):
    N = int(input())

    circles = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))

    visited = [False] * N
    answer = 0

    for i in range(N):
        if not visited[i]:
            bfs(i)
            answer += 1

    print(answer)
