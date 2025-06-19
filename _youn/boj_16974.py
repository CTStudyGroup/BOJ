def countP(level, X, hamburger):
    if level == 0:
        return 1 if X > 0 else 0
    
    if X == 1: return 0
    elif X <= (1 + hamburger[level-1][0]):
        return countP(level-1, X-1, hamburger)
    elif X == (2 + hamburger[level-1][0]):
        return hamburger[level-1][1]+1
    elif X <= (2 + 2* hamburger[level-1][0]):
        return hamburger[level-1][1] + 1 + countP(level-1, X-2-hamburger[level-1][0], hamburger)
    else:
        return hamburger[level][1]
    
def solve(N, X):
    hamburger = [(0,0)]*51
    hamburger[0] = (1, 1) # length, patty num

    for i in range(1, N+1):
        l, n = hamburger[i-1]
        hamburger[i] = (2*l+3, n*2+1)
    
    return countP(N, X, hamburger)

N, X = map(int, input().split())
print(solve(N, X))