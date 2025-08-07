import sys

input = sys.stdin.readline
from collections import deque


def find_cycle(n, s) :
    cycles = set()
    
    for idx in range(1, n+1) :
        if idx in cycles or s[idx] in cycles : continue
        if s == s[idx] : 
            cycles.add(idx)
            continue
        q = deque()
        visited = set()
        visited.add(idx)
        q.append(idx)
        while q :
            A = q.popleft()
            B = s[A]
            if A in cycles  or B in cycles : break
            if A == B : 
                cycles.add(A)    
                break
            if B == idx :
                cycles.add(i for i in visited)
                break
            if B not in visited :
                visited.add(B)
                q.append(B)
    print(cycles)
    return len(cycles)

T = int(input())
for _ in range(T) :
    n = int(input())
    selections = [0]  # 1부터 시작하기 위해
    selections += list(map(int, input().split()))
    cycles = find_cycle(n, selections)
    print(n-cycles)
