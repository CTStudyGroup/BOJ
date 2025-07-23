import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())

# dfs 두번 하면서 공통 depth 최솟값 찾기

def dfs1(node, d):
    if node == 0:
        return

    depth[node] = d
    next_node = tree[node]
    dfs1(next_node, d + 1)

def dfs2(node):
    if depth[node] >= 0:
        print(node)
        return

    next_node = tree[node]
    dfs2(next_node)


for _ in range(T):
    N = int(input())
    tree = [0] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[b] = a  # b의 부모는 a

    # print(tree)

    depth = [-1] * (N + 1)

    n1, n2 = map(int, input().split())
    dfs1(n1, 0)
    dfs2(n2)

