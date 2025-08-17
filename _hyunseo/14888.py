import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -sys.maxsize
min_val = sys.maxsize

def div_toward_zero(a, b):
    if a < 0:
        return - (abs(a) // b)
    return a // b

def dfs(i, curr, p, m, mu, d):
    global max_val, min_val
    if i == N:
        if curr > max_val: max_val = curr
        if curr < min_val: min_val = curr
        return
    x = numbers[i]
    if p:  
        dfs(i+1, curr + x, p-1, m,   mu,  d)
    if m:  
        dfs(i+1, curr - x, p,   m-1, mu,  d)
    if mu: 
        dfs(i+1, curr * x, p,   m,   mu-1,d)
    if d:  
        dfs(i+1, div_toward_zero(curr, x), p, m, mu, d-1)

dfs(1, numbers[0], plus, minus, mul, div)
print(max_val)
print(min_val)
