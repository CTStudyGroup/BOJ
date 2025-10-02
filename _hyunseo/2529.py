import sys


def dfs(n, path) :
    global min_answer, max_answer
    # print(f'n : {n} path : {path}')
    if len(path) == k + 1 :
        path = [str(i) for i in path]
        min_answer = min(min_answer, int(''.join(path)))
        max_answer = max(max_answer, int(''.join(path)))
        return
    if op[n] == "<" :
        for nxt in range(path[-1], 10) :
            if nxt not in path :
                path.append(nxt)
                dfs(n + 1 , path) 
                path.pop()
    elif op[n] == ">" : 
        for nxt in range(0, path[-1]) :
            if nxt not in path :
                path.append(nxt)
                dfs(n+1, path) 
                path.pop()
k = int(input())
op = list(map(str,input().split()))

min_answer, max_answer = sys.maxsize, 0

for i in range(10) :
    dfs(0, [i])
print(max_answer)
if min_answer // 10**k == 0 :
    print('0' + str(min_answer))
else :
    print(min_answer)
