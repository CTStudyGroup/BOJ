import sys
import heapq
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

# 비어있는 자리 중에서 번호 가장 작은 것에 앉음
# 컴퓨터 최소 개수, 각 컴퓨터별 사용한 사람 수

# 시작 시간 순으로 정렬해 앞에서부터 배정
info.sort(key=lambda x: x[0])

using = []  # 사용중인 컴퓨터 우선순위큐 (사용 종료 시간, 컴퓨터 번호) -> 얘는 사용 종료 시간 기준 최솟값을 뽑는 용도
empty = []  # 비어있는 컴퓨터 우선순위큐 (컴퓨터 번호) -> 얘는 컴퓨터 번호 기준 최솟값을 뽑는 용도
computer_users = []  # 컴퓨터별 사용자수

for start, end in info:
    # 현재 시간 기준 using 큐에서 사용 가능한 컴퓨터 뽑아서 empty 큐로 옮김
    while using and using[0][0] <= start:
        _, num = heapq.heappop(using)
        heapq.heappush(empty, num)

    if empty:  # 비어있는 컴퓨터가 있으면
        num = heapq.heappop(empty)  # empty큐에서 하나 뽑아서 사용 처리
        computer_users[num] += 1
    else:  # 비어있는 컴퓨터 없으면
        num = len(computer_users)  # 새 컴퓨터 추가
        computer_users.append(1)

    heapq.heappush(using, (end, num))  # 현재 유저가 사용할 컴퓨터 using 큐에 추가

print(len(computer_users))
print(*computer_users)
