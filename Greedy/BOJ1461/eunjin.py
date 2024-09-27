# 입력 받기
N, M = map(int, input().split())

arr = list(map(int, input().split()))

plus = []
minus = []

for elem in arr:
    if(elem > 0):
        plus.append(elem)
    else:
        minus.append(-elem)

plus = sorted(plus, reverse=True)
minus = sorted(minus, reverse=True)

results = []

for elem in plus[::M]:
    results.append(elem)

for elem in minus[::M]:
    results.append(elem)

print(2*sum(results)-max(results))
