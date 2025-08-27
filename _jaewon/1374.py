# 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지도록 함
# 시작 시간 정렬

import heapq
import sys

N = int(input())
meetings = []
for _ in range(N):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    meetings.append([tmp[1], tmp[2]])
meetings.sort()

first = meetings.pop(0)
queue = [first[1]] # 여기에는 끝나는 시간만 들어간다.
count = 1
maximum = 1

for meeting in meetings:
    # 시작 시간 < 제일 빨리 끝나는 회의 시간
    # 이 경우 무조건 회의실을 추가해야 함
    if(meeting[0] < queue[0]):
        heapq.heappush(queue, meeting[1])
        count += 1
        maximum = max(maximum,count)
    else:
        # 이 경우, 시작 시간보다 빨리 끝나는 회의들을 모두 pop함.
        # 그런 다음, 회의실 queue에 현재 회의를 넣음.
        while queue and meeting[0] >= queue[0]:
            heapq.heappop(queue)
            count -= 1
        heapq.heappush(queue, meeting[1])
        count += 1

print(maximum)


