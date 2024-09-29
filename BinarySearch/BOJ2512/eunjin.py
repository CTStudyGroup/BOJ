# 입력 받기
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

start = 1
end = max(arr)
while start <= end:
    mid = (start+end)//2  # 중앙값 선택
    total = 0  # 중앙값을 기준으로 했을 때 총 예산 금액 합
    for elem in arr:
        if(elem > mid):
            total += mid
        else:
            total += elem
    if(total <= M):  # 중앙값을 키워서 찾기
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)
