N = int(input())
arr = list(map(int, input().split()))

if sum(arr) % 3 != 0:  # 전체 높이가 3씩 성장시켰을 때 나올 수 없는 높이인 경우
    print("NO")
else:
    # 1,2씩 x번 성장시켜야 함
    # 2만큼 성장 시킬 수 있는 횟수가 x번인지
    cnt = 0
    for h in arr:
        cnt += h//2
    if cnt >= sum(arr)/3:
        print("YES")
    else:
        print("NO")
