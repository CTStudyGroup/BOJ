import heapq
import sys

input = sys.stdin.readline

N = int(input())

classes = []

for _ in range(N) :
    n, a, b = map(int, input().split())
    classes.append((a, b))
classes.sort()
q = []
answer = 0
for a, b in classes:
    if not q :
        heapq.heappush(q, b)
        if len(q) > answer :
            answer += 1
            continue
    if q :
        tmp = heapq.heappop(q)
        if tmp <= a :
            heapq.heappush(q, b)
        else :
            heapq.heappush(q, tmp)
            heapq.heappush(q, b)
            if len(q) > answer :
                answer += 1
            
print(answer)
