import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())

arr = []

for _ in range(N):
    command = input().split()
    # print("arr:", arr)

    if command[0] == "push":
        arr.append(command[1])

    if command[0] == "pop":
        print(arr.pop()) if arr else print(-1)

    if command[0] == "size":
        print(len(arr))

    if command[0] == "empty":
        print(0) if arr else print(1)

    if command[0] == "top":
        print(arr[-1]) if arr else print(-1)
