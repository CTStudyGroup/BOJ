from collections import deque

# 입력 받기
N, M = map(int, input().split())

sadari = [[] for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    sadari[x] = y

snake = [[] for _ in range(101)]
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v


INF = int(1e12)

q = deque()
time = [INF for _ in range(101)]

q.append((1, 0))  # x, time
time[1] = 0

while q:
    x, t = q.popleft()
    # print("node: (", x, ",", t, ")")
    for i in range(1, 7):
        next_node = x+i
        if next_node > 100:
            continue
        if sadari[next_node]:
            next_node = sadari[next_node]
        if snake[next_node]:
            next_node = snake[next_node]
        if time[next_node] <= time[x]+1:
            continue
        q.append((next_node, t+1))
        time[next_node] = t+1
        # print("appended node:(", next_node, ",", t+1, ")")

print(time[100])
