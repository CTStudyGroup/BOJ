# M <= 100,000, N <= 100,000
import sys

M, N, L = map(int, input().split())
hunters = list(map(int, input().split()))
hunters.sort()

animals = []
for _ in range(N):
    animals.append(list(map(int,sys.stdin.readline().strip().split())))

animals.sort()

count = 0
current = 0
for animal in animals:
    # 가장 x값이 가까운 hunters로 이동
    while current < M-1:

        if(abs(hunters[current] - animal[0]) > abs(hunters[current+1] - animal[0])):
            current += 1
        else:
            break

    x,y = animal[0], animal[1]
    if((abs(hunters[current]-x) + y) <= L):
        count += 1


print(count)

