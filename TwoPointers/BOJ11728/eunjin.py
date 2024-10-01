# 입력 받기
N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []
# 그냥 정렬 풀이
for elem in A:
    result.append(elem)

for elem in B:
    result.append(elem)

result.sort()
for elem in result:
    print(elem, end=" ")


# 투 포인터 풀이
# a_idx = 0
# b_idx = 0
# while(a_idx < N or b_idx < M):
#     #print("a_idx:", a_idx, ", b_idx:", b_idx)
#     if(a_idx == N):
#         result.append(B[b_idx])
#         b_idx += 1
#     elif(b_idx == M):
#         result.append(A[a_idx])
#         a_idx += 1
#     elif(A[a_idx] > B[b_idx]):
#         result.append(B[b_idx])
#         b_idx += 1
#     elif(A[a_idx] < B[b_idx]):
#         result.append(A[a_idx])
#         a_idx += 1
#     elif(A[a_idx] == B[b_idx]):
#         result.append(A[a_idx])
#         result.append(B[b_idx])
#         a_idx += 1
#         b_idx += 1

# for elem in result:
#     print(elem, end=" ")
