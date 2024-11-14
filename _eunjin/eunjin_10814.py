import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())

age = [0 for _ in range(201)]
arr = []

for _ in range(N):
    x, name = input().split()
    x = int(x)
    arr.append((x, name, age[x]))

    age[x] += 1

# print(arr)


for elem in sorted(arr, key=lambda x: (x[0], x[2])):
    print(elem[0], elem[1])
