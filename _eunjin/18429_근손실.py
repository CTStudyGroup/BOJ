N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 백트래킹
def backtracking(depth):
    global answer, score
    if depth == N:
        answer += 1
        return

    for i in range(N):
        if visited[i]:
            continue

        if score - K + arr[i] >= 500:
            visited[i] = True
            score = score - K + arr[i]
            backtracking(depth + 1)
            score = score + K - arr[i]
            visited[i] = False

visited = [False] * N
answer = 0
score = 500
backtracking(0)
print(answer)
