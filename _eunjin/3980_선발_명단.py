import sys
input = sys.stdin.readline

T = int(input())

# 11명이 있고, 그 11명마다 각각 포지션 할당
# 포지션은 중복 선택이 불가능
# 0~10번에 대한 순열
# 중복 불가

def backtracking(n):
    global answer
    if len(arr) == 11:
        temp = 0
        for i in range(11):
            temp += S[i][arr[i]]
        answer = max(answer, temp)
        return

    for i in range(11):
        if not visited[i] and S[n][i] > 0:
            visited[i] = True
            arr.append(i)
            backtracking(n + 1)
            arr.pop()
            visited[i] = False


for _ in range(T):
    S = [list(map(int, input().split())) for _ in range(11)]
    answer = 0
    arr = []
    visited = [False] * 11
    backtracking(0)
    print(answer)
