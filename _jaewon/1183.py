# 기다리는 시간의 합: sum(|A + T - B|)
# 기다리는 시간의 합이 최소가 되는 T의 개수

import sys

input = sys.stdin.readline

n = int(input())
numbers = list()
for _ in range(n):
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