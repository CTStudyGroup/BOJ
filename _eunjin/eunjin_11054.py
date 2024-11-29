# 입력 받기
N = int(input())

case = list(map(int, input().split()))

increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if case[i] > case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = []

for x in range(N):
    result.append(increase[x]+decrease[x]-1)

# print(result)
print(max(result))
