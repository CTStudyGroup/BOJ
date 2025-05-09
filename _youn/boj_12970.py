def solve(N, K):
    # (1) calculate num of 'A' & 'B'
    a_cnt, b_cnt, minDiff = 0, 0, float('inf')
    for i in range(1,N):
        diff = i*(N-i)-K if i*(N-i) >= K else float('inf')
        if minDiff > diff:
            a_cnt, b_cnt = i, N-i
            minDiff = diff
    if a_cnt*b_cnt < K: return -1

    # (2) find appropriate position of 'B'
    s = ['A']*a_cnt + ['B']*b_cnt
    while minDiff > 0:
        a_count = 0
        for idx, element in enumerate(s):
            if element == 'A': 
                a_count+=1
                a_idx = idx
            elif a_count == 0 and element=='B': continue
            elif a_count > 0 and element == 'B':
                s[idx], s[a_idx] = 'A', 'B'
                break
        minDiff-=1
    return ''.join(s)

N, K = map(int, input().split())
print(solve(N, K))


