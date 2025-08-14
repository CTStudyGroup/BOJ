from collections import deque

S, T = map(int, input().split())

if S == T:
    print(0)
    exit()

# 백트래킹으로 될까??
# 아니다 최소 연산횟수니까 bfs 최단경로처럼 가능할지?

q = deque()
visited = set()

q.append((S, ""))  # node, calc
visited.add(S)

while q:
    node, calc = q.popleft()

    if node > 10e9:
        continue

    if node == T:
        print(calc)
        quit()

    for c in ["*", "+", "-", "/"]:  # 사전순
        if c == "*":
            nxt = node**2
        elif c == "+":
            nxt = node * 2
        elif c == "-":
            nxt = 0
        else:
            if node == 0:
                continue
            nxt = 1

        if nxt not in visited:
            q.append((nxt, calc + c))
            visited.add(nxt)

print(-1)
