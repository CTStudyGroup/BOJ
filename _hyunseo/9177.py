import sys
from collections import Counter
input = sys.stdin.readline

def can_interleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3): 
        return False
    # 빠른 실패 컷
    if Counter(s1) + Counter(s2) != Counter(s3):
        return False

    def dfs(i, j):
        k = i + j
        if k == len(s3):
            return True
        ok = False
        if i < len(s1) and s1[i] == s3[k]:
            ok = ok or dfs(i+1, j)
        if not ok and j < len(s2) and s2[j] == s3[k]:
            ok = ok or dfs(i, j+1)
        return ok

    return dfs(0, 0)

N = int(input())
for n in range(1, N+1):
    s1, s2, s3 = input().split()
    print(f'Data set {n}: {"yes" if can_interleave(s1, s2, s3) else "no"}')
