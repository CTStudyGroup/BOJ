import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
arr = [int(input()) for _ in range(M)]

# 질투심을 k라고 두고, 가능한 k값에 대해 이분 탐색. k는 1~1억까지 가능
# k 1 2 3 ... x-1 x x+1 ...
#   F F F      F  T  T
# 마지막 F 지점을 찾고 거기에 +1 해서 출력하자

# N명의 아이들에게 M가지 색상을 나눠줬을 때 질투심이 k이하가 될 수 있냐
# 있는 보석은 모두 다 나눠줘야 하고, 보석 받지 못하는 아이가 있어도 됨


def is_possiblie(k):
    if(k == 0):
        return False
    num = 0
    for elem in arr:  # 해당 색상을 k개씩 아이에게 나눠주기, k개로 나눠주고도 남은 경우, 아이 1명에게 추가 배정
        num += elem//k + (elem % k != 0)
    return N >= num


curr = -1
step = 10**9
while(step != 0):
    while(curr+step < 10**9+1 and not is_possiblie(curr+step)):
        curr += step
    step //= 2

print(curr+1)
