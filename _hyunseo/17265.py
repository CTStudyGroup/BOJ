import sys


def calculate(curr, path) :
    if path[-2]  == "-" :
        curr -= int(path[-1])
    if path[-2]  == "+" :
        curr += int(path[-1])
    if path[-2]  == "*" :
        curr *= int(path[-1])
    return curr

def dfs(x, y, curr, path) :
    global max_answer, min_answer
    # print(f'x : {x} y : {y} curr : {curr}')
    if x == N-1 and y == N-1 :
        # print(path)
        max_answer = max(max_answer, curr)
        min_answer = min(min_answer, curr)
        return
    tx, ty = x + 1, y
    
    
    if 0 <= tx < N and 0 <= ty < N :
        path.append(grid[ty][tx])
        if grid[ty][tx]=="-" or grid[ty][tx]=="+" or grid[ty][tx]=="*" :
            dfs(tx, ty, curr, path)
        else :
            new_curr = calculate(curr, path)
            dfs(tx, ty, new_curr, path)
        path.pop()
    
    tx, ty = x, y + 1
    if 0 <= tx < N and 0 <= ty < N :
        path.append(grid[ty][tx])
        if grid[ty][tx]=="-" or grid[ty][tx]=="+" or grid[ty][tx]=="*" :
            dfs(tx, ty, curr, path)
        else :
            new_curr = calculate(curr, path)
            dfs(tx, ty, new_curr, path)
        path.pop()

N = int(input())
grid = []
for _ in range(N) :
    grid.append(list(map(str, input().split())))

min_answer, max_answer = sys.maxsize, -sys.maxsize
dfs(0,0,int(grid[0][0]), [int(grid[0][0])])
print(min_answer)
print(max_answer)
