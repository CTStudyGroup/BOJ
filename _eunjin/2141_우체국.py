import sys
input = sys.stdin.readline

N = int(input())
villages = []

total_people = 0

for _ in range(N):
    x, a = map(int, input().split())
    villages.append((x, a))
    total_people += a

villages.sort()

accum = 0
for x, a in villages:
    accum += a
    if accum >= total_people / 2:
        print(x)
        break
