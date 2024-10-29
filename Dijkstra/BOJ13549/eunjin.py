from queue import PriorityQueue

# 입력 받기
N, K = map(int, input().split())

MAX = int(1e5)
INF = int(1e12)
dist = [INF] * (MAX+1)

pq = PriorityQueue()

pq.put([0, N])  # dist, node
dist[N] = 0

while not pq.empty():
    cur_dist, cur_node = pq.get()
    #print("cur_dist:", cur_dist, ", cur_node:", cur_node)
    if(cur_node == K):
        print(cur_dist)
        exit()

    for next_pos in [cur_node-1, cur_node+1]:
        temp_dist = cur_dist+1
        if(0 <= next_pos <= MAX) and (temp_dist < dist[next_pos]):
            dist[next_pos] = temp_dist
            pq.put([temp_dist, next_pos])
            # print("PUT dist:", temp_dist, ", node:", next_pos)

    if(cur_node < K):
        next_pos = cur_node*2
        if(0 < next_pos <= MAX):
            dist[next_pos] = cur_dist
            pq.put([cur_dist, next_pos])
            # print("PUT dist:", cur_dist, ", node:", next_pos)
