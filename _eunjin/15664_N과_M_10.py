N, M = map(int, input().split())
num = list(map(int, input().split()))

num.sort()

answer = []

def backtracking(n, depth):
    # print("bt n:", n, ", depth:", depth, ", arr:", arr)
    if depth == M:
        if arr not in answer:
            answer.append(arr[:])
            return

    for i in range(n, N):
        arr.append(num[i])
        backtracking(i + 1, depth + 1)
        arr.pop()

arr = []
backtracking(0, 0)

for ans in answer:
    print(' '.join(map(str, ans)))
