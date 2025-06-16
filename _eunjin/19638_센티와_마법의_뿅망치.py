import heapq
import sys
input = sys.stdin.readline

N, H, T = map(int, input().split())
arr = []  # 최대 우선순위큐

for _ in range(N):
    h = int(input())
    heapq.heappush(arr, -h)

largest = -1 * heapq.heappop(arr)
if largest < H:
    print("YES")
    print(0)
    exit()

heapq.heappush(arr, -1 * largest)

for t in range(1, T + 1):
    largest = -1 * heapq.heappop(arr)

    if largest == 1:  # 1이면 뿅망치 영향 받지 않음
        heapq.heappush(arr, -1 * largest)
        continue

    heapq.heappush(arr, (-1) * (largest // 2))  # 제일 큰 거인의 키 //2

    largest = -1 * heapq.heappop(arr)  # 제일 큰 거인의 키가 H보다 작으면 YES
    if largest < H:
        print("YES")
        print(t)
        exit()
    heapq.heappush(arr, -1 * (largest))

print("NO")
print(-1 * heapq.heappop(arr))
