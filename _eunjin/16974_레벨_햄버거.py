N, X = map(int, input().split())

# 전체 문자열 만들기엔 크기가 너무 커짐
# 앞에 절반, 뒤에 절반으로 나누어 구하기?
# 나누어 구해도 딱 떨어지지 않는 부분은 어떻게 해야될지

burger = ["" for _ in range(N + 1)]
burger_len = [0 for _ in range(N + 1)]  # 버거 문자열의 총 길이
p_num = [0 for _ in range(N + 1)]  # L-N 버거에서의 패티 총 개수
burger_len[0] = 1
p_num[0] = 1

for i in range(1, N + 1):
    burger_len[i] = 2 * burger_len[i - 1] + 3
    p_num[i] = 2 * p_num[i - 1] + 1

# 틀린 풀이
# def recursion(L, K):  # 레벨 L에서 뒤에서부터 K개 먹을 때 패티의 개수
#     print("L:", L, ", K:", K)
#     if K == 0:
#         return 0
#     if L == 1:
#         print("K:", K)
#         temp = [0, 0, 1, 2, 3, 3]
#         return temp[K]

#     ret = 0
#     start = 0
#     end = burger_len[L] - 1
#     mid = end // 2
#     new_k = K

#     if K == burger_len[L]:  # 버거 전체 다 먹음
#         return 2 * p_num[L - 1] + 1

#     if end - mid <= K:  # 뒤 절반 모두 먹음
#         ret += p_num[L - 1]
#         new_k -= end - mid
#         if mid + 1 <= K:  # 가운데 P 먹음
#             ret += 1
#             new_k -= 1
#         rec = recursion(L - 1, new_k)
#         ret += rec
#         print("-- all half, L:", L, ", rec(", L - 1, ",", new_k, "):", rec, ", ret:", ret)
#     else:
#         rec = recursion(L - 1, K)
#         ret += rec
#         print("-- no half, L:", L, ", rec(", L - 1, ",", K, "):", rec, " ret:", ret)

#     return ret

# 정답 풀이
def recursion(L, K):
    if L <= 1:
        temp = [0, 0, 1, 2, 3, 3]
        return temp[K]

    if K == 1:
        return 0
    elif K <= 1 + burger_len[L - 1]:
        return recursion(L - 1, K - 1)
    elif K == 1 + burger_len[L - 1] + 1:
        return p_num[L - 1] + 1
    elif K <= 1 + burger_len[L - 1] + 1 + burger_len[L - 1]:
        return p_num[L - 1] + 1 + recursion(L - 1, K - (1 + burger_len[L - 1] + 1))
    else:
        return p_num[L]


print(recursion(N, X))
