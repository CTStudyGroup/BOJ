import sys
input = sys.stdin.readline

N = int(input())
rings = list(map(int,input().split()))
rings.sort()
length = len(rings)

# length - 빠지는 개수 - 빠지는 원소의 합 = 1
# 빠지는 원소 합: total

total = 0
count = 0
minimum = N-1
for ring in rings:
    count += 1
    total += ring
    if(length - count - total == 1):
        break
    elif(length - count - total < 1):
        count -= 1
        total = length - count - 1
        break

print(total)
