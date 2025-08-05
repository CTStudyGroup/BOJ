from collections import deque
import heapq
import sys
input = sys.stdin.readline

# 빈 주차장 여러개이면 번호가 가장 작은 공간에 주차
# 주차장에 여러 차 대기중이면 도착 순서대로 주차

N, M = map(int, input().split())
cost = []
weight = []
for _ in range(N):
    cost.append(int(input()))

for _ in range(M):
    weight.append(int(input()))

car_space = [-1] * M  # 각 차량별 배정받은 주차공간 번호
waiting_queue = deque()  # 주차 대기중인 차량 큐
empty = [True] * N  # 각 주차공간 별 사용 가능 여부
answer = 0

for _ in range(2 * M):
    inp = int(input())
    target = -1

    if inp > 0:  # 새로운 차량 들어옴
        waiting_queue.append(inp - 1)
    else:  # 특정 차량 나감
        space = car_space[-inp - 1]  # 해당 차량이 사용한 주차공간 번호
        empty[space] = True
        target = space  # 차량이 나가면 바로 그 공간에 주차 시킨다

    # empty 리스트 돌면서 현재 주차 가능한 공간 있는지 확인
    if target < 0:
        for i in range(N):
            if empty[i]:
                target = i
                break

    # empty 리스트 다 돌았는데도 target 없으면 주차 공간 full
    if target >= 0:
        if waiting_queue:
            car = waiting_queue.popleft()
            car_space[car] = target
            empty[target] = False
            answer += weight[car] * cost[target]

print(answer)
