import sys
from collections import deque

input = sys.stdin.readline

def inorder(n):
    if n > N:  
        return
    inorder(2*n)               # 왼쪽
    tree[n] = q.popleft()      
    inorder(2*n+1)             # 오른쪽

K = int(input())               
N = 2**K - 1                   
q = deque(map(int, input().split()))  
tree = [0] * (N+1)             

inorder(1)

tree = tree
t = 1
while t < len(tree):
    tt = t + 2**(t-1)
    print(*tree[t:tt])
    t = tt
