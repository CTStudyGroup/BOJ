from collections import deque
N = int(input())
score = list(map(int, input().split()))

q = deque([i for i in range(N)])
answer = []
while q:
    idx = q.popleft()
    answer.append(idx + 1)
    sc = score[idx]
    # print("idx:", idx, ", sc:", sc)
    if q:
        if sc > 0:
            for _ in range(sc - 1):
                q.append(q.popleft())
        elif sc < 0:
            for _ in range(-sc):
                q.appendleft(q.pop())
    # print(q)


print(' '.join(map(str, (answer))))
