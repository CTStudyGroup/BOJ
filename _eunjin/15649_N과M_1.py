N, M = map(int, input().split())

def backtracking():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            backtracking()
            arr.pop()
            visited[i] = False

arr = []
visited = [False] * (N + 1)
backtracking()
