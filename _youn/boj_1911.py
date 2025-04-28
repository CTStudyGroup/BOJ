def solve(pool, L):
    ans = 0
    cur_idx = pool[0][0]
    for (start, end) in pool:
        if cur_idx < start:
            cur_idx = start
        count = (end-cur_idx)//L+1
        if (end-cur_idx)%L == 0: count -= 1
        cur_idx += count*L
        ans += count
    return ans

N, L = list(map(int, input().split()))
pool = [tuple(map(int, input().split())) for _ in range(N)]
print(solve(sorted(pool), L))