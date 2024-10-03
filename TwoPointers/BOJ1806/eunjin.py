# 입력 받기
N, S = map(int, input().split())
arr = list(map(int, input().split()))


# 구하고자 하는 최소 길이
min_length = int(1e12)

right = -1
cur_sum = 0
min_sum = 100000000

for left in range(N):

    #print("left:", left, ", right:", right)
    while(right+1 < N) and (cur_sum+arr[right+1] < S):
        right += 1
        cur_sum += arr[right]
        #print("left:", left, ", right:", right, ", cur_sum:", cur_sum)

    if(cur_sum < S and right+1 < N):  # 마지막으로 하나의 원소 더 추가해야되는 경우
        right += 1
        cur_sum += arr[right]
        #print("first if, right:", right, ",cur_sum:", cur_sum)

    if(cur_sum >= S):
        min_length = min(min_length, right-left+1)
        #print("second if, min_length:", min_length)
    cur_sum -= arr[left]


print(min_length if min_length != int(1e12) else 0)
