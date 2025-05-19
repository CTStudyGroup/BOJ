import sys
from collections import deque
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())
for t in range(T):
    print(f'Scenario {t + 1}: ')
    N = int(input())
    K = int(input())

    parent = [j for j in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        union_parent(a, b)

    M = int(input())
    for _ in range(M):
        u, v = map(int, input().split())

        p1 = find_parent(u)
        p2 = find_parent(v)

        if p1 == p2:
            print(1)
        else:
            print(0)

    print()

