import sys
from collections import defaultdict

input = sys.stdin.readline



N , M = map(int, input().split())

parent = list(range(N+1))

def find_parent(a) :
    if parent[a] == a :
        return a
    
    parent[a] = find_parent(parent[a])
    return parent[a]

def join(a, b) :
    root_a = find_parent(a)
    root_b = find_parent(b)
    
    if root_a != root_b :
        if root_a < root_b :
            parent[root_b] = root_a
        else :
            parent[root_a] = root_b
        
        
for _ in range(M) :
    i, j = map(int, input().split())
    join(i, j)

    
timetable = list(map(int, input().split()))


answer = 0

for i in range(N- 1) :
    cur = timetable[i]
    nxt = timetable[i + 1]
    
    if find_parent(cur) != find_parent(nxt) :
        answer += 1
        
print(answer)
