#260113 : [BOJ 20183] 골목 대장 호석 - 효율성 2

import sys, heapq
input = sys.stdin.readline

N, M, A, B, C = map(int, input().split())


adj = [[] for _ in range(N+1)]
MAX_COST = 0
for _ in range(M ) :
    a, b, cost = map(int, input().split())
    MAX_COST = max(cost, MAX_COST)
    adj[b].append((a, cost))
    adj[a].append((b, cost))

def solve(limit) :
    # 주어진 limit이 내가 견딜 수 있는 최대 수치심일 때
    # 내가 가지고 있는 돈 C로 이 길 돌파가 가능한지
    # 가능하면 true, 불가능하면 false

    # 다익스트라 초기화
    distances = [float('inf')] * (N + 1)
    distances[A] = 0
    pq = [(0, A)]  # (누적 비용, 현재 노드)

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if distances[curr_node] < curr_dist:
            continue
        
        if curr_node == B: # 목적지 도착 시 조기 종료 가능
            break

        for next_node, weight in adj[curr_node]:
            # 이번 경로의 가중치(수치심)가 limit보다 크면 아예 지나가지 않음
            if weight <= limit:
                new_dist = curr_dist + weight
                if new_dist < distances[next_node]:
                    distances[next_node] = new_dist
                    heapq.heappush(pq, (new_dist, next_node))
    
    # 도착점까지의 최단 거리 합이 예산 C 이내?
    return distances[B] <= C



l, r = 0, MAX_COST
ans = -1 
while l <= r :
    mid = (l + r ) // 2

    if solve(mid) :
        ans = mid
        r = mid -1
    else :
        l = mid + 1

print(ans)
