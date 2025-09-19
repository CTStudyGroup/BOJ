N, P, Q, X, Y = map(int, input().split())

#⭐️ 250919 : [BOJ 1354] 무한 수열 2 #1920

numbers = {}
def get_A(i) :
    if i <= 0 :
        return 1
    if i in numbers.keys() :
        return numbers[i]
    
    tmp1 =int(i/P)
    tmp2=int(i/Q)
    numbers[i] = get_A(tmp1-X) + get_A(tmp2-Y)
    return numbers[i]

print(get_A(N))
