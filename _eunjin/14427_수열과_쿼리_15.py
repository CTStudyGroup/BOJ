import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

pq = []
for idx, val in enumerate(arr):
    heapq.heappush(pq, (val, idx))  # 1.수열 값 작은 순, 2.인덱스 작은 순

for _ in range(M):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        arr[cmd[1] - 1] = cmd[2]
        heapq.heappush(pq, (cmd[2], cmd[1] - 1))
    else:
        while pq:
            mn_val, mn_idx = heapq.heappop(pq)
            if arr[mn_idx] == mn_val:
                print(mn_idx + 1)
                heapq.heappush(pq, (mn_val, mn_idx))
                break
