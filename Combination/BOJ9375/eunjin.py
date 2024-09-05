from itertools import combinations

# 입력 받기
T = int(input())

for _ in range(T):
    clothes = {}

    N = int(input())
    for _ in range(N):
        line = list(input().split())

        key = line[1]

        # 딕셔너리에서 key에 해당하는 값 가져오기, key 없으면 기본 값 1로 설정
        # 해당 key에 대한 value + 1
        clothes[key] = clothes.get(key, 1)+1

    result = 1
    for v in clothes.values():
        result *= v
    print(result - 1)
