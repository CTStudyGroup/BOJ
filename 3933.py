import sys

input = sys.stdin.readline

MAX_N = 2**15

dp = [0]*(MAX_N + 1)

# print(MAX_N**0.5) -> 182
# 하나의 수로 N을 만들 수 있을 때
for num in range(1, 182) :
    dp[num**2] = 1

# 2개의 수로 N을 만들 수 있을 때
# a <= b 구조
for i in range(1, 182) :
    s1 = i*i
    for j in range(i, 182) :
        s2 = s1 + j*j
        if s2 > MAX_N :
            break
        dp[s2] += 1
        
        
# 3개의 수로 N을 만들 수 있을 떄
# i<= j<= k 구조
for i in range(1, 182) :
    s1 = i*i
    for j in range(i, 182) :
        s2 = s1 + j*j
        if s2 > MAX_N :
            break
        for k in range(j, 182) :
            s3 = s2 + k*k
            if s3 > MAX_N :
                break
            dp[s3] += 1
#4개의 수로 N을 만들 수 있을 때
# i <= j <= k<= t
for i in range(1, 182) :
    s1 = i*i
    for j in range(i, 182) :
        s2 = s1 + j*j
        if s2 > MAX_N :
            break
        for k in range(j, 182) :
            s3 = s2 + k*k
            if s3 > MAX_N :
                break
            for t in range(k, 182) :
                s4 = s3 + t*t
                if s4 > MAX_N :
                    break
                dp[s4] += 1
print("--")           
while True :
    n = int(input())
    if n == 0 :
        sys.exit()
    print((dp[n]))
        
