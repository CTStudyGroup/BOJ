import math

def solve(k):
    ans = 0
    while k > 0:
        x = int(math.log2(k))
        ans ^= 1
        k -= 1 << x
    return ans

k = int(input())
print(solve(k-1))
