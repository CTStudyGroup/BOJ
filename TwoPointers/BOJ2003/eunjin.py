# 입력 받기
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 누적합 array 생성
arr = [0]
for i in range(N):
    arr.append(arr[i]+A[i])

# print(arr)
cnt = 0


for i in range(N+1):
    value = arr[i]
    find_value = value + M
    start = i
    end = N
    while(start <= end):
        mid = (start+end)//2
        if(arr[mid] > find_value):
            end = mid-1
        if(arr[mid] < find_value):
            start = mid+1
        if(arr[mid] == find_value):
            cnt += 1
            #print("i:", i, ", mid:", mid)
            break

print(cnt)
