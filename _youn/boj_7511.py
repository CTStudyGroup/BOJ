from collections import defaultdict

def Find(x, relation):
    if relation[x]<0: return x
    relation[x] = Find(relation[x], relation)
    return relation[x]

def Union(u, v, relation):
    u = Find(u, relation)
    v = Find(v, relation)
    if u==v: # don't need to proceed union
        return False
    relation[v] = u
    return True # union complete!

tc = int(input())
for i in range(1, tc+1):
    n = int(input())
    k = int(input())

    relation = defaultdict(lambda: -1)
    for _ in range(k):
        u, v = map(int, input().split())
        Union(u, v, relation)

    m = int(input())
    ans = []
    for _ in range(m):
        u, v = map(int, input().split())
        ans.append(int(Find(u, relation)==Find(v, relation)))
    
    print(f"Scenario {i}:")
    print(*ans,sep='\n')
    print()