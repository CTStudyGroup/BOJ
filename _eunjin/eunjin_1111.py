N = int(input())
arr = list(map(int, input().split()))

# N==1이면 다음 수는 무엇이든 될 수 있다.
if N == 1:
    print("A")
    exit()

if N == 2:
    if arr[0] == arr[1]:  # X X X X.. 이렇게 계속 같은 수
        print(arr[0])
    else:
        print("A")  # 서로 다른 수 2개 만으로는 다음에 뭐가 올지 특정할 수 없음
    exit()


# 첫번째, 두번째 수를 가지고 A와 B 특정하기
# arr[x+1] = A * arr[x] + B
A = 0
B = 0
if arr[0] == arr[1]:
    A = 0
else:
    A = (arr[2] - arr[1]) // (arr[1] - arr[0])

B = arr[1] - arr[0] * A

# 두번째 ~ 끝까지 모든 수가 A와 B 공식 만족하는지 확인
for i in range(1, N - 1):
    expected = arr[i] * A + B
    if arr[i + 1] != expected:
        print("B")
        exit()

print(arr[-1] * A + B)
