from collections import deque

N = int(input())
arr = list(map(int, input().split()))

# 1~N 순열을 다시 복구 하는 문제
# 1: appendleft
# 2: popleft + appendleft + appendleft
# 3: append

q = deque()

for i in range(N):
    n = arr[N - i - 1]
    if n == 1:
        q.appendleft(i + 1)
    elif n == 2:
        temp = q.popleft()
        q.appendleft(i + 1)
        q.appendleft(temp)
        # q.insert(1, i + 1)
    else:
        q.append(i + 1)

print(' '.join(map(str, q)))

help(deque)
