N = int(input())
K = int(input())
coor = sorted(set(map(int, input().split())))
dist = []

for i in range(1, len(coor)):
    dist.append(abs(coor[i-1]-coor[i]))
dist = sorted(dist)
idx = len(dist)-(K-1)
print(sum(dist[:idx]))