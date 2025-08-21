import heapq

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]

# 시작 시간 기준 정렬
classes.sort(key=lambda x: x[0])

running = 

for start, end in classes:
    if running and running[0] <= start:  #
        heapq.heappop(running)          
    
    heapq.heappush(running, end)  

print(len(running))
