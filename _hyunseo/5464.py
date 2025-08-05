'''
1~N 주차 공간

매일 아침 비어있을 때 시작
차가 오면 -> 비어있는 자리가 있는지 확인
if 비어있는 공간 X : 입구에서 대기
elif 주차 공간 하나, 빈 공간 없다가 하나 생기면 : 바로 주차
else 빈 공간 많으면 : 번호가 가장 작은 주차 공간에 주차

여러대의 차량은 deque()로 관리. first come first out

주차료는 주차한 시간이 아닌, 차량의 무게에 비례
주차료 = 차량의 무게 * 공간마다 책정된 단위 무게당 요금

M대의 차량이 주차장을 이용할 것을 알고, 차량이 입출 순서 알아

총 수입을 계산해야 함. '''

import sys
from collections import deque

input = sys.stdin.readline

# N :주차 공간 수 , M : 차량 수
N, M = map(int, input().split())
# 주차 공간들의 단위 무게당 요금
price_per_weight = [int(input()) for _ in range(N)]
# 차량 무게들 (1! 부터 시작해서 M까지)
car_weight = [int(input()) for _ in range(M)]
car_weight = deque(car_weight)
car_weight.appendleft(0)
# 나가는 순서
orders = [int(input()) for _ in range(M*2)]

# 사전 정의
total = 0  # 총 수입
waiting_line = deque()  # 주차장 입구 대기 차들
parking_space = [0] * N # 현재 주차된 차 수
for order in orders :
    print(f'parking_space : {parking_space}')
    # 입차하는 경우
    if order > 0 :
        # 주차했는지의 여부
        flag = 0
        
        for idx, space in enumerate(parking_space) :
            if space == 0 :
                flag = 1  # 주차했음!
                parking_space[idx] = order  # 차 세우고
                total += car_weight[order]*price_per_weight[idx]  # 금액 받고
                break
        if flag == 0 :  #주차 자리가 없었던 경우
            waiting_line.append(order)  # 대기
    # 출차하는 경우
    else : 
        order = abs(order)
        for idx, space in enumerate(parking_space) :
            if space == order :
                parking_space[idx] = 0
                break
        if waiting_line :
            next_car = waiting_line.popleft()
            parking_space[idx] = next_car
            total += car_weight[next_car]*price_per_weight[idx]
            
print(total)
