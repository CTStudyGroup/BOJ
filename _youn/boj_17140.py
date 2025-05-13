from collections import defaultdict

def check(r, c, k, A):
    if r >= len(A) or c >= len(A[0]):
        return False
    return A[r][c]==k

def R(A):
    maxlength = 0
    # (1) sort by row
    for i in range(len(A)):
        num = defaultdict(int)
        for v in A[i]:
            if v == 0: continue
            num[v] += 1
        num = sorted(num.items(), key=lambda x: (x[1],x[0]))
        A[i] = [item for pair in num for item in pair]
        if len(A[i])>100: A[i] = A[i][:100]
        maxlength = max(maxlength, len(A[i]))

    # (2) interpolate 0
    for i in range(len(A)):
        if len(A[i])<maxlength:
            A[i] += [0]*(maxlength-len(A[i]))

def C(A):
    A[:] = list(map(list, zip(*A)))
    R(A)
    A[:] = list(map(list, zip(*A)))
    
def solve(r, c, k, A):
    for t in range(101):
        if check(r, c, k, A): return t
        if len(A)>=len(A[0]): R(A)
        else: C(A)
    return -1

# Input
r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
# Solve
print(solve(r-1, c-1, k, A))