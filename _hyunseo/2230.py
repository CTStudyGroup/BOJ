import sys

input = sys.stdin.readline


N, M = map(int, input().split())
nums  =[]
for _ in range(N) :
    nums.append(int(input()))
nums.sort()
answer = sys.maxsize
l, r = 0, 0
while r < N :
    diff = nums[r]-nums[l]
    if diff >= M : 
        answer = min(answer, diff)
        if answer == M :
            print(M)
            sys.exit()
    
    if diff < M :
        r += 1
    elif diff > M :
        l += 1
print(answer)
