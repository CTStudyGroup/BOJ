N,K = map(int, input().split())

prices = []
times = []

for _ in range(N):
    time1, price1, time2, price2 = map(int, input().split())
    prices.append((price1, price2))
    times.append((time1, time2))

maximum = 0
def backtrack(path, depth, time_sum):
    global maximum
    if(depth == N):
        total = 0
        for index, target in enumerate(path):
            total += prices[index][target]
        maximum = max(maximum,total)    
        return
    
    # time_sum은 지금까지 누적 시간
    walk, bike = times[depth]
    if(time_sum + walk <= K):
        path.append(0)
        time_sum += walk
        backtrack(path, depth + 1, time_sum)
        path.pop(-1)
        time_sum -= walk

    if(time_sum + bike <= K):
        path.append(1)
        time_sum += bike
        backtrack(path, depth + 1, time_sum)
        path.pop(-1)
        time_sum -= bike

backtrack([],0,0)
print(maximum)

    
