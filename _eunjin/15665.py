N, M = map(int, input().split())
num = list(map(int, input().split()))

result = set()

def dfs(depth, arr):
    if depth == M:
        result.add(tuple(arr))
        return

    for i in range(N):
        arr.append(num[i])
        dfs(depth + 1, arr)
        del arr[-1]

dfs(0, [])

result_arr = list(result)
result_arr.sort()

for elem in result_arr:
    print(' '.join(map(str, elem)))
