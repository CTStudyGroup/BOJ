from collections import deque

N, M = map(int, input().split())
temp = list(map(int, input().split()))

T = temp[0]
truth = []
for i in range(1, T+1):
    truth.append(temp[i])


party = []
adj_list = [[] for _ in range(N+1)]  # 파티로 인해 연결된 사람들 인접리스트

for _ in range(M):
    temp = list(map(int, input().split()))
    n = temp[0]
    people = temp[1:]
    party.append(people)

    for i in range(n):
        for k in range(n):
            if i != k:
                adj_list[people[i]].append(people[k])


# print("truth:", truth)
# print("party:", party)
# print("adj_list:", adj_list)


# 진실을 아는 사람과 같은 파티에 참석한 사람들까지 전부 포함한 리스트 생성
truth_total = truth[:]

for node in truth:
    q = deque()
    visited = [False]*(N+1)

    q.append(node)
    visited[node] = True

    while q:
        curr_node = q.popleft()

        for adj_node in adj_list[curr_node]:
            if visited[adj_node]:
                continue
            q.append(adj_node)
            truth_total.append(adj_node)
            visited[adj_node] = True

# print("truth_total:", truth_total)

# 각 파티마다의 참석자와 truth_total을 비교해 참석자가 truth_total에 있는 경우, 카운트 세지 않음
cnt = 0
for i in range(M):
    people = party[i]
    b = True
    for p in people:
        if p in truth_total:
            b = False
            break

    if b:
        cnt += 1

print(cnt)
