from collections import defaultdict
import sys

N, M = map(int, sys.stdin.readline().strip().split())

keywords = defaultdict(bool)

for _ in range(N):
    keyword = input()
    keywords[keyword] = True

count = N
for _ in range(M):
    written = list(sys.stdin.readline().strip().split(','))
    length = len(written)
    for i in range(length):
        if(keywords[written[i]]):
            keywords[written[i]] = False
            count -= 1
    
    print(count)