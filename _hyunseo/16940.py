from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 노드 수
N = int(input())

# 방문 기록 
visited = [0] *( N+1)

# 연결 리스트 관리
graph = defaultdict(list)
for _ in range(N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 주어진 BFS 문장
given = list(map(int, input().split()))

# 1로 시작 안하는 경우는 미리 0 출력, 끝내기
if given[0] != 1 :
    print(0)
    exit()

# 다음으로 방문한 부모 노드는 deque로 관리
par = deque()
# BFS 문장 인덱스 관리
idx = 0
# 처음 방문할 1은 미리 deque에 추가, 방문 처리
par.append(given[0])
visited[1] = 1

# 문장을 다 훑거나, par가 빈 경우
while par and idx < len(given):
    # 다음으로 방문한 부모 노드
    parent = par.popleft()
    # 부모 노드와 연결된 노드 중 방문되지 않은 노드만 children set에 넣기
    # -> list였을 때는 시간 초과, set으로 바꾸니 시간 초과 해결
    c = list(graph[parent])
    children = set()
    for child in c :
        if visited[child] == 0 :
            children.add(child)
          
    # 연결된 모든 자식 노드 순회
    while children :
        # 주어진 문장 인덱스(문장 상 다음으로 방문할 노드)
        curr = given[idx + 1]
        if curr not in children :
            print(0)
            sys.exit()
        else :
            par.append(curr)
            children.remove(curr)
            idx += 1
            visited[curr] = 1
print(1)
