from collections import deque

MAX = int(1e5)

# 입력 받기
N, K = map(int, input().split())

q = deque()
visited = [False] * (MAX+1)

q.append((0, N))  # (time, position)
visited[N] = True

while q:
    time, pos = q.popleft()

    if pos == K:
        print(time)
        exit()

    for next_pos in [pos-1, pos+1, pos*2]:
        if(0 <= next_pos <= MAX) and (not visited[next_pos]):
            q.append((time+1, next_pos))
            visited[next_pos] = True
