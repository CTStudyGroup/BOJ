N, M = map(int, input().split())

# 중복X, 오름차순

def backtracking(n):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(n + 1, N + 1):
        # if not visited[i]:
        #     arr.append(i)
        #     visited[i] = True
        #     backtracking(i)
        #     arr.pop()
        #     visited[i] = False
        arr.append(i)
        backtracking(i)
        arr.pop()

arr = []
visited = [False] * (N + 1)
backtracking(0)

