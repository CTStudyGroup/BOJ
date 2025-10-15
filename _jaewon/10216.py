# 노드를 연결리스트(딕셔너리)로 표현
# 그 다음에 bfs count를 사용

import sys
import math
input = sys.stdin.readline

T = int(input())

def bfs(start, graph, visited):
    visited[start] = 1
    queue = []
    queue.append(graph[start])

    while queue:
        adj_list = queue.pop(0) # 인접한 노드들의 배열

        for node in adj_list:
            if(visited[node]):
                continue

            visited[node] = 1
            queue.append(graph[node])



for _ in range(T):
    N = int(input())
    xyr = []    
    dic = {}
    # adj = [[0 for _ in range(N)] for _ in range(N)] # 인접 행렬

    for i in range(N):
        x,y,r = map(int, input().split())
        xyr.append((x,y,r))
        dic[i] = list()

        if (i == 0):
            continue
        
        # 이전에 저장되어 있는 좌표들과 연결되어 있는지 확인
        for j in range(i):
            bx, by, br = xyr[j]
            # 연결되어 있다면
            if(math.sqrt((x-bx)**2 + (y-by)**2) <= (r + br)):
                dic[i].append(j)
                dic[j].append(i)

    count = 0
    visited = [0 for _ in range(N)]
    for i in range(N):
        if (visited[i] == 0):
            bfs(i, dic, visited)
            count += 1
    
    print(count)