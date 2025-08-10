# 트리 사용
# 땅의 개수 N
# 오리의 수 Q

N, Q = map(int, input().split(" "))
wants = [int(input()) for _ in range(Q)]

occupied = {}

for want in wants:
    current = want

    flag = False
    minimum = []
    while(current != 1):
        if(current in occupied):
            flag = True
            minimum.append(current)
        current = current // 2
    
    if(flag):
        print(minimum[-1])
        continue

    occupied[want] = 1
    print(0)