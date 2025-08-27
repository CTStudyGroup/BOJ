import sys

input = sys.stdin.readline

N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def backtrack(start, total, depth, cnt) :
    global answer 
    if L<= total <= R and cnt >= 2:
        if arr[depth] - arr[start] >= X :
            answer += 1
    if total > R :
        return 
    for next in range(depth + 1, N) :
        backtrack(start, total + arr[next], next, cnt + 1)
        

answer = 0
for i in range(N-1) :
    backtrack(i, arr[i], i, 1)
print(answer)
