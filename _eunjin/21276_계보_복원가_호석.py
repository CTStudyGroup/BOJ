import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())
names = list(input().split())

# 이름: 인덱스 매핑
names.sort()
idx = {}
for i, name in enumerate(names):
    idx[name] = i

# 위상정렬
M = int(input())
adj_list = [[] for _ in range(N)]
indegree = [0] * N

for _ in range(M):
    a, b = input().split()
    # b -> a (b가 a의 조상)
    adj_list[idx[b]].append(idx[a])
    indegree[idx[a]] += 1

# print(names)
# print(adj_list)

# 최상위 조상 찾기
roots = []
q = deque()
for i in range(N):
    if indegree[i] == 0:
        roots.append(names[i])
        q.append(i)


children = defaultdict(list)  # 직계 자식 기록용 dict

while q:
    cur = q.popleft()
    for nxt in adj_list[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:  # 진입차수가 0이 되는 노드만 다음 탐색 대상
            children[names[cur]].append(names[nxt])
            q.append(nxt)

roots.sort()
print(len(roots))
print(*roots)

for name in names:
    kids = sorted(children[name])
    print(name, len(kids), *kids)
