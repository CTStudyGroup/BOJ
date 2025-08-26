import sys
import heapq
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    _, a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()  # 시작 시간 순으로 정렬

pq = []  # 강의 종료 시간  우선순위큐
answer = 0

for start, end in arr:
    if pq:  # 기존 강의실 있는 경우
        earliest_end = heapq.heappop(pq)
        # print("end:", end, " earliest:", earliest_end)
        if start >= earliest_end:  # 해당 강의실 재사용 가능
            heapq.heappush(pq, end)
        else:  # 새 강의실 추가 배정
            heapq.heappush(pq, earliest_end)
            heapq.heappush(pq, end)
            answer += 1
    else:  # 기존 강의실 없는 경우
        heapq.heappush(pq, end)
        answer += 1

print(answer)
