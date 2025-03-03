T = int(input())

def solve(N, prices):
    ret = 0
    mx = 0
    for i in range(N - 1, -1, -1):
        if prices[i] > mx:
            mx = prices[i]
        else:
            ret += mx - prices[i]
    return ret


for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    print(solve(N, prices))
