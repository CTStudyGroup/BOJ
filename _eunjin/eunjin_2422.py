# 완전탐색
N, M = map(int, input().split())
ban = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    ban[a - 1].append(b - 1)
    ban[b - 1].append(a - 1)

answer = 0

def dfs(depth, n, k):
    global answer
    if depth == 3:
        answer += 1
        return

    if k == -1:
        for i in range(n + 1, N):
            if i not in ban[n]:
                dfs(depth + 1, i, n)
    else:
        for i in range(n + 1, N):
            if i not in ban[n] and i not in ban[k]:
                dfs(depth + 1, i, n)

for n in range(N):
    dfs(1, n, -1)
print(answer)
