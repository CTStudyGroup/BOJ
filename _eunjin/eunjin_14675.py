import sys
input = sys.stdin.readline

N = int(input())
adj_node = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_node[a].append(b)
    adj_node[b].append(a)

Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())

    if t == 1:
        if len(adj_node[k]) >= 2:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
