from itertools import permutations
# 입력 받기
N = int(input())
A = list(map(int, input().split()))

count = {}

count["plus"], count["minus"], count["mult"], count["div"] = map(
    int, (input().split()))

calc = []
for key in count:
    for _ in range(count[key]):
        calc.append(key)

maxValue = -10**9
minValue = 10**9

# 각 순열에 대해 값 계산
for operator in set(permutations(calc)):
    result = A[0]
    for i in range(0, N-1):
        if(operator[i] == "plus"):
            result += A[i+1]
            continue
        if(operator[i] == "minus"):
            result -= A[i+1]
            continue
        if(operator[i] == 'mult'):
            result *= A[i+1]
            continue
        if(operator[i] == "div"):
            if(result < 0):
                result = -(abs(result)//A[i+1])
            else:
                result = result//A[i+1]

    # 최소값, 최대값 업데이트
    if(result > maxValue):
        maxValue = result

    if(result < minValue):
        minValue = result

print(maxValue)
print(minValue)
