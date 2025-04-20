import sys
input = sys.stdin.readline

N = int(input())

# 주어진 입력에는 중복이 있을 수 있지만, 출력은 중복이 없어야 한다.
# 같은 depth에 대해서는 같은 원소 고르면 안된다.

def backtracking():
    if len(arr) == M:
        print(''.join(arr))
        return

    prev = -1
    for i in range(M):
        if string[i] == prev or visited[i]:
            continue
        arr.append(string[i])
        visited[i] = True
        prev = string[i]
        backtracking()
        arr.pop()
        visited[i] = False


for _ in range(N):
    string = list(input().strip())
    string.sort()
    M = len(string)
    arr = []
    visited = [False] * M
    backtracking()
