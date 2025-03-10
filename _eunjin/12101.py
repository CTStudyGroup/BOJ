N, K = map(int, input().split())

result = []

def backtracking(n, arr):
    if n == 0:
        result.append(arr[:])
    if n < 0:
        return

    if len(result) >= K:
        return

    for i in range(1, 4):
        arr.append(i)
        backtracking(n - i, arr)
        del arr[-1]



backtracking(N, [])

if len(result) < K:
    print(-1)
else:
    print('+'.join(map(str, result[K - 1])))
