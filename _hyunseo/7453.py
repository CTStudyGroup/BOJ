import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

A, B, C, D = [], [], [], []

for _ in range(n) :
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

dic = defaultdict(int)
for a in A:
    for b in B:
        dic[a+b] += 1
count = 0
for c in C:
    for d in D:
        count += dic.get(-(c+d), 0)  # defaultdict보다 get()이 조금 더 빠름

print(count)
