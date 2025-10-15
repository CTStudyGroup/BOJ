# 목표: 주차장의 총 수입 계산
# 주차료 = 차량 무게 * 단위 무게당 요금

# N: 주차 공간 수
# M: 차량 수
# prices[]: 주차 공간의 단위 무게당 요금 배열
# weights[]: 차량들의 무게 배열
# seq[]: 차량들의 출입부(양 - push, 음 - pop)
# spaces[]: 주차 공간 배역ㄹ

(N, M) = map(int,input().split(' '))
spaces = [0 for _ in range(N)]
prices = [0 for _ in range(N)]
seq = [0 for _ in range(M*2)]
weights = [0 for _ in range(M+1)]
        
for i in range(N):
    price = int(input())
    prices[i] = price

# 무게 배열에서 index 0은 사용하지 않음
for i in range(1, M+1):
    weight = int(input())
    weights[i] = weight

for i in range(M*2):
    seq[i] = int(input())

parking = [False for _ in range(N)]

def sol():
    queue = {}
    waiting = []
    total = 0
    for i in range(len(seq)):
        if (seq[i] > 0):
            # 주차장이 꽉 차 있으면 대기
            if (parking.count(True) == N):
                waiting.append(seq[i])
                continue 

            park_index = parking.index(False)
            parking[park_index] = True
            price = prices[park_index]
            queue[seq[i]] = (price, park_index)
        else:
            (price, park_index) = queue[abs(seq[i])]
            weight = weights[abs(seq[i])]
            total += weight * price

            parking[park_index] = False

            # 대기자가 있는 경우 처리
            if(len(waiting) != 0):
                park_index = parking.index(False)
                parking[park_index] = True
                price = prices[park_index]
                queue[waiting.pop(0)] = (price, park_index)
    print(total)

sol()