import math

K = int(input())
if math.log2(K) %1 == 0 :
    print(K, 0)
    exit()
k = int(math.log2(K))
#필요한 최소 초콜릿의 크기
N = 2**int(k+1)
#필요한 최소 초콜릿의 루트 클기 (즉 2**n = N)
n=k+1
k = int(K)

for i in range(n,-1,-1) :
    if k - 2**i >= 0 :
        
        k -= 2**i
    if i == 0 :
        

        print(N, n)
        break
    if k == 0 :
        

        print(N, n - i)
        break
