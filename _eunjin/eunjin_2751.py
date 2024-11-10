import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

for n in sorted(arr):
    print(n)
