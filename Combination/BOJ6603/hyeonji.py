from itertools import combinations
import sys
input=sys.stdin.readline

while 1:
    test_case=list(map(int,input().split()))

    if test_case[0]==0:
        break

    k=test_case[0]
    s=test_case[1:]

    case=list(combinations(s,6))

    for i in case:
        print(*list(i))

    print()