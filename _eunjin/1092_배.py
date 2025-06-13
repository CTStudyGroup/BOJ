N = int(input())
crain = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

crain = sorted(crain, reverse=True)
box = sorted(box, reverse=True)

if crain[0] < box[0]:
    print(-1)
    exit()

# 각 크레인마다 남은 박스 중 가장 무거운 박스 할당
answer = 0

while box:
    for c in crain:
        if box and c < box[-1]:  # 가장 가벼운 박스도 못드는 경우 해당 크레인 skip
            continue
        for b in box:
            if c >= b:  # 해당 박스 들 수 있는 경우
                box.remove(b)
                break
    answer += 1

print(answer)
