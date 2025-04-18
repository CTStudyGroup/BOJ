N, M = map(int, input().split())

# 중복 순열, 비내림차순

def backtracking(n):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(n, N + 1):
        arr.append(i)
        backtracking(i)
        arr.pop()

arr = []
backtracking(1)
