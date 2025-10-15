# union find로 루트를 구함.
import sys

N = int(input())

parent = [0] * (10**6 + 1)
size = [1] * (10**6 + 1)

def find_root(node):
    if (parent[node] == 0):
        return node
    else:
        while True:
            next = parent[node]
            if(next == 0):
                return node
            else:
                node = next

def add_union(root1, root2):
    if(root1 < root2):
        parent[root2] = root1
        size[root1] += size[root2]
        size[root2] = 0
    elif(root1 > root2):
        parent[root1] = root2
        size[root2] += size[root1]
        size[root1] = 0
    else:
        return
    
for _ in range(N):
    instruction = list(sys.stdin.readline().strip().split())

    if (instruction[0] == 'I'):
        root1 = find_root(int(instruction[1]))
        root2 = find_root(int(instruction[2]))
        
        add_union(root1, root2)
    else:
        rx = find_root(int(instruction[1]))
        print(size[rx])



