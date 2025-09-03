import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

tree = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a] = [b, c]


def dfs(i):
    global answer

    # 왼쪽 자식 노드
    left = tree[i][0]
    if left >= 0 and not visited[left]:
        answer += 1
        dfs(left)

    visited[i] = True  # 현재 노드 방문

    if i == last:  # 현재 노드가 순회의 끝인 경우
        print(answer)
        return

    # 오른쪽 자식 노드
    right = tree[i][1]
    if right >= 0 and not visited[right]:
        answer += 1
        dfs(right)

    answer += 1

# 순회의 끝 노드 찾기
curr, last = 1, 1
while True:
    if tree[curr][1] == -1:
        last = curr
        break
    curr = tree[curr][1]

dfs(1)
