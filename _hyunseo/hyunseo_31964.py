from collections import deque

N = int(input())
X = list(map(int, input().split()))
T = list(map(int, input().split()))

d = []
for _ in range(N) :
    d.append((X[_], T[_]))
d.sort(reverse=True)
# print(d)
time = max(d[0][0], d[0][1])
place = d[0][0]
for x,t in d[1:] :
    if t <= time + abs(place - x) :
        
        time += abs(place - x)
        place = x
    else :
        place = x
        time = max(t,time +abs(place - x)  )
    # print(f'time : {time} place : {place}')
print(time + place )
