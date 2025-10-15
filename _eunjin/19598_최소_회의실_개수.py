import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 일단 주어진 arr을 시작 시간순으로 정렬
# 우선순위큐에 각 회의실 회의 종료 시간 저장
# 새 회의마다 큐에서 가장 빨리 회의 끝나는 회의실 뽑기
# - 회의 종료시간이 새 회의의 회의 시작 시간보다 작거나 같으면 해당 회의실 이용 가능
# - 회의 종료시간이 새 회의의 회의 시작 시간보다 크면 새 회의실 추가 배정

arr.sort()

pq = []
answer = 0

for start, end in arr:
    if pq:
        fastest = heapq.heappop(pq)  # 가장 빨리 회의 끝나는 회의실의 종료시간 뽑기
        if fastest <= start:  # 해당 회의실 이용 가능
            heapq.heappush(pq, end)
        else:
            heapq.heappush(pq, fastest)  # 회의실 다시 넣기
            heapq.heappush(pq, end)  # 회의실 추가 배정
            answer = max(answer, len(pq))
    else:  # 새 회의실 배정
        heapq.heappush(pq, end)
        answer = max(answer, len(pq))


print(answer)
