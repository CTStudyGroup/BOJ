n = int(input())
graph = dict()
for i in range(n):
    a, _, b = list(input().split())
    graph[a] = b

m = int(input())
for i in range(m):
    a, _, b = list(input().split())

    visited = set()
    while True:
        if a not in graph or a in visited:
            print("F")
            break
        if graph[a] == b:
            print("T")
            break
        visited.add(a)
        a = graph[a]
