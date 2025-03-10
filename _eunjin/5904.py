# N = int(input())

# def getN(K):
#     if K == 0:
#         return 3

#     return getN(K - 1) * 2 + K + 3

# # N 길이가 되려면 K가 몇까지 가능한지..
# def getK(N):
#     for i in range(28):
#         n = getN(i)
#         if n >= N:
#             return i

# def recursive(x):
#     if x == 0:
#         return "moo"

#     temp = recursive(x - 1)

#     return temp + "m" + "o" * (x + 2) + temp

# K = getK(N)
# string = recursive(K)
# print(string[N - 1])

# 위 풀이는 메모리 초과


# N = int(input())

# # m의 인덱스만 리스트로 저장하자

# arr = [0]

# def getN(K):
#     if K == 0:
#         return 3

#     return getN(K - 1) * 2 + K + 3

# # N 길이가 되려면 K가 몇까지 가능한지
# def getK(N):
#     for i in range(28):
#         n = getN(i)
#         if n >= N:
#             return i

# def recursive(x):
#     if x == 0:
#         return 3

#     n = recursive(x - 1)
#     temp_arr = []

#     for i in arr:
#         temp_arr.append(n + x + 3 + i)

#     arr.append(n)  # m 인덱스 추가
#     arr.extend(temp_arr)  # 나머지 반쪽 m 인덱스 추가

#     return n * 2 + x + 3

# K = getK(N)
# recursive(K)
# if N in arr:
#     print("m")
# else:
#     print("o")

# 이것도 메모리 초과

N = int(input())

# 현재 총 길이, 가운데 길이, 구하려는 순서
def recursive(total_length, mid_length, N):
    if N <= 3:
        return "moo"[N - 1]

    # 왼쪽 수열 길이 = 가운데를 제외한 반
    left_length = (total_length - mid_length) // 2

    # 찾으려는 순서가 왼쪽 수열에 있으면 -> 그 전 수열로
    if N <= left_length:
        return recursive(left_length, mid_length - 1, N)

    # 찾으려는 순서가 오른쪽 수열에 있으면 -> 왼쪽 수열의 순서로 바꾸고 그 전 수열로
    if N > left_length + mid_length:
        return recursive(left_length, mid_length - 1, N - left_length - mid_length)

    # 찾으려는 순서가 가운데에 위치할 때
    # 찾으려는 순서가 가운데의 첫번째면 m, 아니면 o
    if N - left_length == 1:
        return "m"
    else:
        return "o"


total_length = 3  # 처음에는 moo 세글자
n = 0  # 몇번째 수열인지 -> 가운데 길이 구하기 위함
while total_length < N:
    # 기존 수열 * 2 + o 개수 + m 개수
    n += 1
    total_length = 2 * total_length + n + 3

# 가운데 길이 = 수열 순서 + 3
print(recursive(total_length, n + 3, N))

