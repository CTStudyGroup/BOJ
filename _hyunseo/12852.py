import sys

sys.setrecursionlimit(10**6)
from collections import deque

N = int(input())

q = deque()

q.append((N, 0, [N]))
record = [N]*(N+1)
while q :
    num, cnt , path= q.popleft()
    if num == 1 :
        print(cnt)
        print(*path)
        sys.exit()
    if num % 3 == 0 :
        if record[num//3] > cnt + 1 :
            path.append(num//3)
            q.append((num//3, cnt + 1, path[:]))
            path.pop()
            record[num//3] = cnt + 1
    if num % 2 == 0 :
        if record[num//2] > cnt + 1 :
            path.append(num//2)
            q.append((num//2, cnt + 1, path[:]))
            path.pop()
            record[num//2] = cnt + 1
    if record[num-1] > cnt + 1 :
        path.append(num-1)
        q.append((num - 1, cnt + 1, path[:]))
        path.pop()
        record[num-1] = cnt + 1
