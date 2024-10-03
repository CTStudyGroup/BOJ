# 입력 받기
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 배열에 들어있는 수가 1~10000 사이의 값임
# 구간의 점수의 최댓값의 최솟값을 x라고 두고, 이 x가 0~9999 사이에 어떤 값인지 찾자
# F F F F ... F T T .. T T 이렇게 될 것임

# 구간의 점수의 최댓값을 x이하가 되도록 M개 이하의 구간으로 나눌 수 있느냐


def is_possible(x):
    global N, M, arr
    curr_min = arr[0]
    curr_max = arr[0]
    cnt = 0  # 구간 기준점의 개수

    for i in range(N):
        curr_min = min(curr_min, arr[i])
        curr_max = max(curr_max, arr[i])

        if(curr_max-curr_min > x):  # 구간 점수가 x보다 크면 구간 나눈다.
            cnt += 1  # 구간의 개수를 하나 늘리고
            curr_min = arr[i]  # 지금 인덱스부터 새 구간 시작하기
            curr_max = arr[i]
    cnt += 1

    return cnt <= M


curr = -1
step = 10000
while(step != 0):
    while(curr+step <= 9999 and not is_possible(curr+step)):
        curr += step
    step //= 2
    # print("cur:", curr)

print(curr+1)
