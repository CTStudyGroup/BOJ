import sys

input = sys.stdin.readline

def solve(x, n, lst ) :
    x = x * (10**7)
    
    lst.sort()
    
    l, r = 0, n-1
    
    while l < r :
        if lst[l] + lst[r] == x :
            return [True, lst[l], lst[r]]
        elif lst[l] + lst[r] < x :
            l += 1
        else :
            r -= 1
    return [False]
    
# T = int(input())
while True :
    try:
        X = int(input())
    except (EOFError, ValueError): # 입력이 없거나 빈 문자열이면
        break # 루프 종료
    
    N = int(input())
    legos = []
    for _ in range(N) :
        legos.append(int(input()))
    
    s = solve(X, N, legos)
    if s[0] :
        print(f'yes {s[1]} {s[2]}')
    else :
        print('danger')
