from queue import PriorityQueue
import sys
input = sys.stdin.readline

# 입력 받기
V, E = map(int, input().split())
start_node = int(input())

adj_list = [[] for _ in range(V+1)]
INF = int(1e12)
dist = [INF] * (V+1)
dist[0] = 0

# 인접리스트 생성
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append([w, v])  # dist, next_node

pq = PriorityQueue()
pq.put([0, start_node])
dist[start_node] = 0

while not pq.empty():
    curr_dist, curr_node = pq.get()
    for adj_dist, adj_node in adj_list[curr_node]:
        temp_dist = curr_dist+adj_dist
        if(temp_dist < dist[adj_node]):
            dist[adj_node] = temp_dist
            pq.put([temp_dist, adj_node])


for elem in dist[1:]:
    if(elem == INF):
        print("INF")
    else:
        print(elem)
