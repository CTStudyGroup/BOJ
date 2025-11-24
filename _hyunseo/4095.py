import sys

input = sys.stdin.readline




while True :
    N, M = map(int, input().split())
    if N == 0 and M == 0 :
        sys.exit()
    
    grid = []
    for _ in range(N) :
        grid.append(list(map(int, input().split())))
    
    status = [[0]*M for _ in range(N) ]
    for x in range(M ) :
        cnt = 0
        for y in range(N-1, -1, -1) :
            if grid[y][x] == 0 :
                cnt = 0
            else :
                cnt += grid[y][x]
            status[y][x] = cnt
    
    answer = 0
    MAX_ANSWER = min(N, M)
    
    
    for y in range(N) :
        for x in range(M) :
            if status[y][x] <= answer :
                continue
            
            min_h = status[y][x]
            
            
            for l in range(M-x) :
                min_h = min(min_h, status[y][x+l])
                
                width = l + 1
                side = min(min_h, width)
                answer = max(answer, side)
                
                if width > min_h :
                    break
    print(answer)
    
