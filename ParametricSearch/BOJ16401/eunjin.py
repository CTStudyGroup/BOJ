# 입력 받기
M, N = map(int, input().split())
L = list(map(int, input().split()))

# 답이 될 수 있는 과자의 길이를 k라고 두었을 때
# k는 1부터 10억까지 가능, O(logN)으로 풀어야 한다
# 파라매트릭 서치로 풀자

# 가능한 최대 막대 과자 길이를 구해야 한다
# k 1 2 3 ... x-1 x x+1 ...
#   T T T      T  T  F

# M명의 조카에게 과자 길이가 k이하가 되도록 모두 나누어줄 수 있는지


def is_possible(k):
    global M, N, L
    if(k == 0):
        return False

    cnt = 0
    for elem in L:
        cnt += elem//k
    # print("cnt:", cnt)
    return cnt >= M


curr = -1
step = max(L)+1

while(step != 0):
    #print("curr+step:", curr+step, ", curr:", curr, ", step:", step)
    while(curr+step < max(L)+1 and is_possible(curr+step)):
        curr += step
    step //= 2

print(curr if curr > 0 else 0)
