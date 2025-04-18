import heapq

N = int(input())

q = []
for _ in range(N):
    arr = list(map(int, input().split()))
    for i in range(N):
        if len(q) < N:
            heapq.heappush(q, arr[i])
        else:
            if arr[i] > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, arr[i])
        # print(q)

print(q[0])
