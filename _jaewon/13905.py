import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa != pb:
        parent[pb] = pa

def main():
    N, M = map(int, input().split())
    s, e = map(int, input().split())

    edges = [tuple(map(int, input().split())) for _ in range(M)]
    # (from, to, weight)
    edges.sort(key=lambda x: x[2], reverse=True)  # 내림차순 정렬

    global parent
    parent = list(range(N + 1))

    for u, v, w in edges:
        union(u, v)
        if find(s) == find(e):
            print(w)
            return

    print(0)

if __name__ == "__main__":
    main()
