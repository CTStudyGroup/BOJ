from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

# flag 두고 버리는 연산, 옮기는 연산 반복
# 남은 길이가 1될때까지
q = deque([i for i in range(1, N + 1)])
flag = 0
while len(q) > 1:
    if flag:
        n = q.popleft()
        q.append(n)
        flag = not flag
    else:
        q.popleft()
        flag = not flag

print(q[0])
