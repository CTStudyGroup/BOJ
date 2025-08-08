import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

parent = [-1] * (N + 1)
for i in range(2, N + 1):
    parent[i] = i // 2

used = [False] * (N + 1)

# w -> root 노드까지 올라가면서 first_used 갱신
def able(w):
    node = w
    first_used = 0
    while True:
        if node == 1:
            break

        if used[node]:
            first_used = node

        node = parent[node]

    return first_used

# w -> root로 거슬러 올라갈 수 있는지
for _ in range(Q):
    w = int(input())
    first_used = able(w)
    if first_used <= 0:
        used[w] = True
        print(0)
    else:
        print(first_used)
