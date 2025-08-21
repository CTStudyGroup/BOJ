# N은 100,000까지. N^2 불가능
import heapq
import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    time.append(tuple(map(int,input().split())))

time.sort(key=lambda x: x[0])

# 회의의 끝나는 시간을 저장하는 배열
# 큐의 길이 == 회의실의 최소 개수
queue = []
heapq.heappush(queue, time[0][1])

for i in range(1, N):
    start, end = time[i]

    # 가장 빨리 끝나는 회의실이 현재 회의 시작 전에 끝났다면 → 회의실 재사용
    if queue[0] <= start:
        heapq.heappop(queue)

    # 현재 회의 끝나는 시간 push
    heapq.heappush(queue, end)

print(len(queue))