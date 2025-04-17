from collections import deque

N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]

q = deque(arr)

t = 0
answer = []

# q에 남은 원소 있을 때까지
while q:
    n = q.popleft()
    t += 1
    if t == K:
        answer.append(n)
        t = 0
    else:
        q.append(n)


print('<' + ', '.join(map(str, answer)) + '>')
