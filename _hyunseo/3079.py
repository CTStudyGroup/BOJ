import sys

input = sys.stdin.readline

N, M = map(int, input().split())
station = []
for _ in range(N) :
  a = int(input())
  station.append(a)
station.sort()

left = 0
right = station[-1]*M

def check(time) :
      cnt = 0 
      for s in station :
            if s <= time :
                  cnt += (time // s)
      return cnt
    
    
while left < right :
  mid = (left + right) // 2

  if check(mid) >= M : #이 시간안에 끝낼 수 있으면
    right = mid
  else :
    left = mid + 1
    
print(left)
