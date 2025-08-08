import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
occupied = [0] * (N + 1)

for _ in range(Q):
    land = int(input())
    cur = land
    blocker = 0
    
    while cur > 0:
        if occupied[cur]:
            blocker = cur 
        cur //= 2

    if blocker == 0:
        occupied[land] = 1  
        print(0)
    else:
        print(blocker)
