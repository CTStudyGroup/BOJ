N = int(input().strip())

small = []
big = []

for _ in range(N-1):
    x, y = map(int,input().split())

    small.append(x)
    big.append(y)

biggest = int(input())

minimum = 10**9
def backtrack(index, power, used):
    # used는 슈퍼 점프를 썼는지 여부
    global minimum
    if(index == N):
        minimum = min(minimum, power)
        return

    backtrack(index+1, power + small[index-1], used)

    if(index + 2 <= N):
        backtrack(index+2, power + big[index-1], used)
    
    if(index + 3 <= N and not used):
        used = True
        backtrack(index+3, power + biggest, used)
        used = False

backtrack(1,0,False)
print(minimum)