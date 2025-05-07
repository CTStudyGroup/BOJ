def solve(N, students):
    dp = [0]*N
    for i in range(N): # end
        min_s, max_s = students[i], students[i]
        for j in range(i, -1, -1): # start
            min_s = min(min_s, students[j])
            max_s = max(max_s, students[j])
            if (i-j)+1 >=2:
                prev = dp[j-1] if j > 0 else 0
                dp[i] = max(dp[i], prev + (max_s-min_s))
    return max(dp)

N = int(input())
students = list(map(int, input().split()))
print(solve(N, students))
