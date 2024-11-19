# 입력 받기
N = int(input())

INF = int(1e5)

answer = INF

if N % 5 == 0:
    answer = min(answer, N//5)

for x in range((N//5)+1):
    if (N-5*x) % 3 == 0:
        answer = min(answer, x + (N-5*x)//3)

if N % 3 == 0:
    answer = min(answer, N//3)

print(-1 if answer == INF else answer)
