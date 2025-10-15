import sys
input = sys.stdin.readline

N = int(input())
books = [int(input()) for _ in range(N)]

mx_idx = books.index(N)

# 제일 큰 책 오른쪽의 책들은 전부 이동 대상
answer = N - mx_idx - 1

# 제일 큰 책 왼쪽의 책들은 전부 1씩 차이나면서 내림차순 정렬되어 있어야 함
n = N
for i in range(mx_idx - 1, -1, -1):
    if books[i] + 1 != n:
        answer += 1
    else:
        n = books[i]

print(answer)
