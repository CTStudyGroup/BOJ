# 입력 받기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

X = max(max(A), max(B))
answer = []
for i in range(X, 0, -1):
    while True:
        if i not in A or i not in B:
            break

        answer.append(i)
        A = A[A.index(i)+1:]
        B = B[B.index(i)+1:]


print(len(answer))
print(' '.join(map(str, answer)))
