import sys
input = sys.stdin.readline
N = int(input())
weight = list(map(int, input().split()))

def backtracking(arr, w):
    global answer
    if len(arr) == N - 2:
        answer = max(answer, sum(arr))
        return

    for i in range(1, len(w) - 1):
        arr.append(w[i - 1] * w[i + 1])
        backtracking(arr, w[:i] + w[i + 1:])
        arr.pop()

answer = 0
backtracking([], weight)
print(answer)
