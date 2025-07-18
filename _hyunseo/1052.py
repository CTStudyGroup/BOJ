N, K = map(int, input().split())

# num보다 큰 2의 제곱 중 가장 작은 2의 제곱 반환
def get_two(num):
    two = 1
    while two < num :
        two *= 2
    return two

def water_bottle(n, k) :
    if k >= n :return 0
    two = get_two (n)
    if k == 1 : return two - n
    
    return water_bottle(n-two//2, k-1)
sum = 0
sum += water_bottle(N, K)

print(sum)
