from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
parent_ = [0] * (N+1)
time = [0] * (N+1)
dp = [0] * (N+1)

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    t = arr[0]
    cnt = arr[1]
    time[i] = t
    for pre in arr[2:]:
        graph[pre].append(i)
        parent_[i] += 1

q = deque()

for i in range(1, N+1):
    if parent_[i] == 0:
        q.append(i)
        dp[i] = time[i]

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        parent_[nxt] -= 1
        dp[nxt] = max(dp[nxt], dp[cur] + time[nxt])
        if parent_[nxt] == 0:
            q.append(nxt)

print(max(dp[1:]))
