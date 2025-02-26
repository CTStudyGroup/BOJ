def backtracking(n, start, total):
    if n == 0:
        result.add(total)
        return
    for i in range(start, 4):
        backtracking(n-1, i, total+num[i])


N = int(input())
num = [1, 5, 10, 50]
result = set()
backtracking(N, 0, 0)
# print(result)
print(len(result))
