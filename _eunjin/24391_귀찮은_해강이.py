import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
parent = [i for i in range(N + 1)]

# 주어진 시간표에 대해 이전 건물과 현재 건물이 서로 연결되어있는지 여부 알아야 함
# 유니온 파인드로 각 건물의 최고 조상 번호 구하기

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
    union(a, b)

answer = 0
timeline = list(map(int, input().split()))
for i in range(1, len(timeline)):
    if find(timeline[i]) != find(timeline[i - 1]):
        answer += 1

print(answer)
