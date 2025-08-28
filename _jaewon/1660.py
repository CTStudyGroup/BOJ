# 사면체의 최소 개수
# DP?

N = int(input())

nums = []
tri = []
quat = []
s = 0
acc = 0
for i in range(1, 300):
    s += i
    tri.append(s) 

for t in tri:
    acc += t
    if acc > N:
        break
    quat.append(acc)

dp = [10**9 for _ in range(N+1)]
dp[0] = 0
for size in quat:
    dp[size] = 1

for i in range(1, N+1):
    for size in quat:
        if(i>size):
            dp[i] = min(dp[i], dp[i-size] + 1)
        else:
            break

print(dp[N])