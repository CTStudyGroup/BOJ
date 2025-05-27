from collections import defaultdict

def solve(W, K):
    index = defaultdict(list)
    for i, w in enumerate(W):
        index[w].append(i)
    
    ans = [float('inf'), -1]
    for k in index.keys():
        if len(index[k])<K: continue
        for i in range(len(index[k])-K+1):
            length = index[k][i+K-1]-index[k][i]+1
            ans[0] = min(ans[0], length)
            ans[1] = max(ans[1], length)
    return ans if ans[1]!=-1 else [-1]
        
T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    print(*solve(W, K))