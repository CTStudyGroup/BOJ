def solve(A, K, weight):
    if len(A)==1: # base case
        global count
        count+=1
        return
    
    weight -= K
    for idx in range(len(A)):
        if weight+A[idx] >= 500:
            solve(A[:idx]+A[idx+1:], K, weight+A[idx])
    
# Input
N, K = map(int, input().split())
A = list(map(int, input().split()))
# Solve
count = 0
solve(A, K, 500)
print(count)