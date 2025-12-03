N, M = map(int, input().split())
lst = list(map(int, input().split()))

# max_arr = [[0]*(N+1) for _ in range(N+1)]
# min_arr = [[10000]*(N+1) for _ in range(N+1)]
# K = [[0]*N for _ in range(N)]

# for i in range(N) :
#     for j in range(i+1, N+1) :
#         min_arr[i][j]= min(lst[i:j+1])
#         max_arr[i][j]= max(lst[i:j+1])
#         K[i][j] = max_arr[i][j] - min_arr[i][j]

# 주어진 길이로 최대 몇개가 나오나요?
def possible(n) :
    cnt = 0 
    tmp = [lst[0], lst[0]]
    
    for i in range(1, N) :
        tmp[0] = min(tmp[0], lst[i])
        tmp[1] = max(tmp[1], lst[i])
        if tmp[1] - tmp[0] > n :
            cnt += 1
            tmp= [lst[i], lst[i]]
    return cnt + 1

# 역 이분법
l, r= 0, max(lst)- min(lst)


while l < r :
    mid = (l + r) // 2
    
    if possible(mid) <= M :
        r = mid
    else :
        l = mid + 1
print(r)
