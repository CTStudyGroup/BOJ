import sys
input = sys.stdin.readline

N, X = map(int, input().split())

burger = {} # (버거 길이, 패티 수)
burger[0] = (1, 1)
for i in range(1, N+1):
    burger[i] = (burger[i-1][0]*2 + 3, burger[i-1][1]*2 + 1)

def patties(index, n):
    res = 0

    if (index == 0):
        return 0
    
    if (n == 0): # n==0일 때 index가 1이면 아래의 if문에서 런타임 에러 발생
        return 1

    # 절반이상 먹는 경우
    if(index >= burger[n][0]/2):
        res = burger[n-1][1] + 1 # n-1번째 햄버거 패티 수 + 1
        res += patties(index-2-burger[n-1][0], n-1)
    else:
        res += patties(index-1, n-1) # 제일 앞 번 제거해서 아래 단계로

    return res

print(patties(X, N))
