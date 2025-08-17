import math
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
n = N
bin_N = str(bin(n))[2:]

added = 0

while bin_N.count('1') > K :
    added += 1
    n += 1
    bin_N = str(bin(n))[2:]
    
print(added)
