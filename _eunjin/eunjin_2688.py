# 시간 초과 풀이
import sys
input = sys.stdin.readline

T = int(input())

def dfs(n, depth):
    global answer
    if depth == N:
        answer += 1
        return

    for i in range(n, 10):
        dfs(i, depth + 1)


for _ in range(T):
    N = int(input())
    answer = 0
    dfs(0, 0)
    print(answer)
