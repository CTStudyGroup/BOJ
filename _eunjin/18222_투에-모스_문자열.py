K = int(input())

def solve(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n % 2 == 0:
        return solve(n // 2)

    if n % 2 == 1:
        return 1 - solve(n // 2)

print(solve(K - 1))

