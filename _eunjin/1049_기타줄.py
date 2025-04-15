N, M = map(int, input().split())
package = []
one = []
for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    one.append(b)

package.sort()
one.sort()

# 패키지만
p = N // 6
p_price = package[0] * p

if N % 6 > 0:
    p_price += package[0]

# 패키지 + 낱개
b_price = package[0] * p + one[0] * (N - p * 6)

# 낱개만
o_price = one[0] * N

print(min(p_price, b_price, o_price))
