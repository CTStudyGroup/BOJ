def search_digits(N, k): # search digits
    count = 0
    for i in range(len(str(N))):
        digit_count = min(N, 10**(i+1)-1) - 10**i + 1
        count += digit_count * (i + 1)
        if k <= count: return i, count - digit_count * (i + 1)
    return -1, 0

def get_count(mid, digits): # get count of [10^digits ~ mid]
    return (digits+1) * (mid - 10**(digits) + 1)
    
def solve(N, k):
    digits, count = search_digits(N, k)
    if digits == -1: return -1
    else:
        left, right = 10**digits, 10**(digits+1)-1
        while left <= right:
            mid = (left + right)//2

            total_count = count + get_count(mid, digits)
            if  total_count < k:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        idx = count + get_count(ans, digits) - k + 1
        return str(ans)[-idx]

N, k = map(int,input().split())
print(solve(N, k))