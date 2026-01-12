import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

total = sum(lst)

if total % 4 != 0:
    print(0)
else:
    target = total // 4
    cnt1 = 0 # 1/4 지점 개수
    cnt2 = 0 # 2/4 지점 개수
    ans = 0  # 3/4 지점 개수
    
    curr = 0
    for i in range(N - 1):
        curr += lst[i]

        if curr == 3 * target:
            ans += cnt2
            
        if curr == 2 * target:
            cnt2 += cnt1
            
        if curr == 1 * target:
            cnt1 += 1
            
    print(ans)
