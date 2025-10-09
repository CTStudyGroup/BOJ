import sys
input = sys.stdin.readline

N = int(input())

# 일단 T를 완탐으로 구할 순 없을 것 같은데
# 그리디인가??
# 그냥 A와 B의 차이 절댓값이 큰거 ~ 작은거 사이 전부가 다 최솟값이 되는건가?
# -> 이건 아닌듯

# 모르겠다........

numbers = list()
for _ in range(N):
    a, b = map(int, input().split())
    numbers.append(b - a)

numbers = sorted(numbers)

answer = 0
if len(numbers) % 2 == 0:
    start = len(numbers) // 2 - 1
    answer = numbers[start + 1] - numbers[start] + 1
else:
    answer = 1

print(answer)
