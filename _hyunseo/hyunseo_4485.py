# 250704 : [BOJ 4485] 녹색 옷 입은 애가 젤다지? #1362
import heapq

prob_num = 0


while True :
    N = int(input())
    if N == 0 :
        break
    board = []
    for _ in range(N) :
        board.append(list(map(int, input().split())))
        
    dist = [[126]*N for _ in range(N)]
    dist[0][0] = board[0][0]
    
    hq = []
    heapq.heappush(hq, (board[0][0], 0, 0))
    while hq :
        cost, y,x = heapq.heappop(hq)
        
        if dist[y][x] < cost :
            continue
        for dy, dx in [(-1,0), (1, 0), (0,-1), (0,1)]  :
            ny, nx = y+dy, x + dx
            if 0<= nx < N and 0 <= ny < N :
                next_cost = cost + board[ny][nx]
                if next_cost < dist[ny][nx] :
                    dist[ny][nx]  = next_cost
                    heapq.heappush(hq, (next_cost, ny,nx))
    prob_num += 1
    print(f"Problem {prob_num}: {dist[N-1][N-1]}")
