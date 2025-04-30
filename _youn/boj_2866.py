def can_remove_row(k, R, C, strings):
    seen = set()
    for j in range(C):
        word = ''.join(strings[i][j] for i in range(k, R))
        if word in seen:
            return False
        seen.add(word)
    return True

def solve(R, C, strings):
    left, right, ans = 0, R - 1, 0
    while left <= right:
        mid = (left + right) // 2
        if can_remove_row(mid, R, C, strings):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

R, C = list(map(int, input().split()))
strings = [input() for _ in range(R)]
print(solve(R, C, strings))