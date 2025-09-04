import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
left = {}
right = {}

for _ in range(N):
    a, b, c = map(int, input().split())
    left[a] = b
    right[a] = c

# 1. 중위 순회 마지막 노드 찾기
def inorder_last(node):
    if right[node] != -1:
        return inorder_last(right[node])
    return node

last = inorder_last(1)  # 루트는 항상 1번

# 2. 루트에서 마지막 노드까지 거리 구하기 (DFS)
def dist(u, target, d=0):
    if u == -1:
        return -1
    if u == target:
        return d
    # 왼쪽에서 찾기
    ld = dist(left[u], target, d+1)
    if ld != -1:
        return ld
    # 오른쪽에서 찾기
    rd = dist(right[u], target, d+1)
    if rd != -1:
        return rd
    return -1

d = dist(1, last)

# 3. 정답 계산
answer = 2 * (N - 1) - d
print(answer)
