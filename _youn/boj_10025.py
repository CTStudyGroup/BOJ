from collections import defaultdict

def solve(K, board, endx):
    ans, val = 0, sum([board[i] for i in range(K)])
    for i in range(endx+1):
        if i <= K: val += board[i+K]
        else: val = val + board[i+K] - board[i-K-1]
        ans = max(ans, val)
    return ans

N, K = map(int, input().split())
board, endx = defaultdict(int), 0
for _ in range(N):
    g, x = map(int, input().split())
    board[x] = g
    endx = max(endx, x)
print(solve(K, board, endx))