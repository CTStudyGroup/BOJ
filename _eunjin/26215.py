import heapq

N = int(input())
snow = list(map(int, input().split()))

# 최대 힙 구성 (음수 사용하여 max-heap 역할 수행)
heap = [-x for x in snow]
heapq.heapify(heap)

answer = 0

# 가장 높은 두 개를 계속 제거
while len(heap) > 1:
    a = -heapq.heappop(heap)
    b = -heapq.heappop(heap)

    answer += 1

    # 남은 눈이 있으면 다시 넣기
    if a - 1 > 0:
        heapq.heappush(heap, -(a - 1))
    if b - 1 > 0:
        heapq.heappush(heap, -(b - 1))

# 마지막 남은 눈이 있으면 그 값만큼 추가
if heap:
    answer += -heap[0]

# 1440분 초과하면 -1 반환
print(answer if answer <= 1440 else -1)
