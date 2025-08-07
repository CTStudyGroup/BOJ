import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque


def dfs(curr) :
    global count
    # 현재 노드 방문 처리
    visited[curr] = 1
    # 다음 노드
    dst = selections[curr]
    
    #다음 노드가 아직 방문 X 
    if visited[dst] == 0 :
        dfs(dst)
    elif not finished[dst] :
        # 사이클
        tmp = dst
        cycle_size = 1
        while tmp != curr :
            tmp = selections[tmp]
            cycle_size += 1
        count += cycle_size
    finished[curr] = 1

T = int(input())
for _ in range(T) :
    n = int(input())
    selections = [0] + list(map(int, input().split()))
    visited=[0]*(n+1)
    finished = [0]*(n+1)
    count = 0
    for idx in range(1, n+1) :
        if visited[idx] == 0 :
            dfs(idx)
    print(n - count)
