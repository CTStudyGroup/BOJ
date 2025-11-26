import sys

input = sys.stdin.readline


S = input().strip()
S_lst = list(S)
from collections import deque

q = deque()
lst = []
for idx, val in enumerate(S) :
    if val == "(" :
        q.append(idx)
    if val == ")" :
        bef_idx = q.pop()
        lst.append([bef_idx, idx])

answer = set()

from itertools import combinations as comb

for num in range(1, len(lst) + 1) :
    options = list(comb(lst, num))
    
    for option in options :
        target = []
        for a, b in option :
            target.append(a)
            target.append(b)
        target.sort(reverse = True)
        
        tmp = S_lst[:]
        for t in target :
            tmp.pop(t)
        answer.add(''.join(tmp))

answer = sorted(list(answer))
for line in answer :
    print(line)

