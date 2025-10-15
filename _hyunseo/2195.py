import sys
input = sys.stdin.readline

S = input().strip()
P = input().strip()

def solve(S, P):
    n, m = len(S), len(P)
    i = 0   # 현재 P에서 만들 위치
    answer = 0
    while i < m:
        length = 0
        for j in range(n):
            k = 0
            while i + k < m and j + k < n and P[i+k] == S[j+k]:
                k += 1
            length = max(length, k)
        answer += 1
        i += length
    return answer

print(solve(S, P))
