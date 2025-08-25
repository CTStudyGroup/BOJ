import sys

input = sys.stdin.readline
from collections import Counter
from itertools import permutations


def solve(chars_count ) :
    def dfs(path) :
        if len(path) == len(chars) :
            answer.add(path)
            return
        for k in chars_count :
            if chars_count[k] > 0 :
                chars_count[k] -= 1
                dfs(path+k)
                chars_count[k] += 1
                    
    
    answer = set()
    dfs('')
    for a in sorted( answer) :
        print(a)
N = int(input())
for _ in range(N) :
    chars = list(input().strip())
    chars_count = Counter(chars)
    answer = set()
    solve(chars_count)
    
