N = int(input())
MOD = 1000000000

# dp
# F(n)=F(n-1)+F(n-2)
# F(n-2)=F(n)-F(n-1)
dp1 = [0] * 1000001  # 양수 dp
dp2 = [0] * 1000001  # 음수 dp

dp1[1] = 1  # F(1)
dp2[1] = 1  # F(-1)
# F(-1) = F(1)-F(0) = 1
# F(0) = F(-1)+F(-2), F(-2)=-1
# F(-1) = F(-2)+F(-3), F(-3)=2
# F(-2) = F(-3)+F(-4), F(-4)=-3

for i in range(2, 1000001):
    dp1[i] = (dp1[i - 1] + dp1[i - 2]) % MOD

for i in range(2, 1000001):
    temp = dp2[i - 2] - dp2[i - 1]
    if temp < 0:
        dp2[i] = abs(temp) % MOD * (-1)
    else:
        dp2[i] = temp % MOD

if N == 0:
    print(0)
    print(0)
elif N < 0:
    if dp2[-N] > 0:
        print(1)
    else:
        print(-1)
    print(abs(dp2[-N]) % MOD)
else:
    if dp1[N] > 0:
        print(1)
    else:
        print(-1)
    print(abs(dp1[N]) % MOD)
