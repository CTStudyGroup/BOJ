import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

# 유니온 파인드

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    parent[b] = a
    _dict[a] += _dict[b]  # 부품 개수 누적

parent = [i for i in range(10**6 + 1)]  # 부모 리스트 자기 자신으로 초기화
_dict = defaultdict(lambda: 1)


for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == "I":
        a = int(cmd[1])
        b = int(cmd[2])
        union(a, b)
    else:
        c = int(cmd[1])
        print(_dict[find(c)])
