# 입력 받기
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# N이 100,000까지 가능하고, 강의의 길이도 최대 10,000까지 가능하므로 브루트포스 풀이는 불가
# 블루레이 크기를 1분 ~10000*100000분까지의 값을 탐색하되, 이분탐색으로 하자


# 블루레이 크기가 k일 때 arr을 M개 구간으로 나눌 수 있느냐
def is_possible(k):
    global N, M, arr
    cnt = 0
    sum_value = 0
    for i in range(N):
        if(arr[i] > k):  # 강의 하나의 길이가 블루레이 크기보다 큰 경우
            return False

        if(sum_value+arr[i] <= k):  # i번째 강의가 기존 구간에 포함될 수 있는 경우
            sum_value += arr[i]
        else:  # i번째 강의가 기존 구간에 포함될 수 없는 경우
            cnt += 1  # 구간 개수를 늘리고
            sum_value = arr[i]  # 강의 길이의 합 초기화

    # print("cnt+1:", cnt+1)
    return cnt+1 <= M


curr = -1
step = 10000*100000+1
while(step != 0):
    # print("curr:", curr, ", step:", step)
    # print("length:", step+curr, ", is_possible:", is_possible(step+curr))
    while(curr+step <= 10000*100000 and not is_possible(step+curr)):
        curr += step
    step //= 2

print(curr+1)
