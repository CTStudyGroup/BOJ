# 입력 받기
N = int(input())
arr = list(map(int, input().split()))


# 틀린 풀이
# -1 -2 4 98 -99
# arr = sorted(arr, key=lambda x: abs(x))
# print(arr)

# min_value = int(1e12)
# cur_sum = int(1e12)
# right = 0
# min_left = 0
# min_right = 0

# for left in range(N):
#     print("============================")
#     print("left:", left, ", right:", right)
#     while(right+1 < N) and (abs(arr[left]+arr[right+1]) <= cur_sum):
#         right += 1
#         print("abs(arr[left]+arr[right]):",
#               abs(arr[left]+arr[right]), ", cur_sum:", cur_sum)
#         cur_sum = abs(arr[left]+arr[right])
#         min_left = left
#         min_right = right
#         print("left:", left, ", right:", right, ", cur_sum:", cur_sum,
#               ", min_left:", min_left, ", min_right:", min_right)
#     right -= 1

# print(min_left)
# print(min_right)

# result = []
# result.append(arr[min_left])
# result.append(arr[min_right])
# result.sort()
# for elem in result:
#     print(elem, end=" ")

# 정답 풀이
arr = sorted(arr)

start = 0
end = N-1
ans_sum = abs(arr[start]+arr[end])
ans = [arr[start], arr[end]]

while(start < end):
    #print("start:", start, ",end:", end)
    left = arr[start]
    right = arr[end]

    cur_sum = left + right
    if abs(cur_sum) < ans_sum:
        ans_sum = abs(cur_sum)
        ans = [left, right]
        if(ans_sum == 0):
            break

    if cur_sum < 0:
        start += 1  # cur_sum이 음수이면 0에 가까워지기 위해 start+1
    else:
        end -= 1  # cur_sum이 양수이면 0에 가까워지기 위해 end-1

print(ans[0], ans[1])
