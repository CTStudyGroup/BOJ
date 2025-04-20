def greedy(mid, M, K):
    count = 1
    money = mid

    for val in K:
        if money < val:
            count += 1
            money = mid
        money -= val
    return count<=M

def binarySearch(N, M, K):
    low = max(K)
    high = sum(K)
    while low <= high:
        mid = (low+high)//2
        if greedy(mid, M, K):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

N, M = list(map(int, input().split()))
K = [int(input()) for _ in range(N)]
print(binarySearch(N, M, K))