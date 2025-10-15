# ⭐️ 250826 : [BOJ 18116] 로봇 조립 
import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
input = sys.stdin.readline
MAXN = 1000000  # 로봇 최대 번호

parent = [i for i in range(MAXN+1)]
size = [1] * (MAXN+1)

# union find
def count_parent(node):
    root = find_parent(node)
    cnt = 0
    for i in range(len(parent)):
        if find_parent(i) == root:
            cnt += 1
    return cnt
def find_parent(node) :
    if parent[node] != node :
        return find_parent(parent[node])
    return node
def union(node1, node2) :
    node1 = find_parent(node1)
    node2 = find_parent(node2)
    if node1 == node2 : return
    
    if size[node1] < size[node2] :
        parent[node1] = node2
        size[node2] += size[node1]
    else :
        parent[node2] = node1
        size[node1] += size[node2]


N = int(input())
out = []

for _ in range(N):
    order = input().split()
    if order[0] == b"I":  # buffer 입력이라 문자열이 아니라 bytes
        a, b = int(order[1]), int(order[2])
        union(a, b)
    else:  # Q
        a = int(order[1])
        out.append(str(size[find_parent(a)]))

write("\n".join(out))
