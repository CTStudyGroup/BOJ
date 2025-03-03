A, B = map(int, input().split())

# 백트래킹
# depth를 더해가며 2 곱하기 + 오른쪽에 1 추가하기
# B가 완성되면 depth를 리턴

result = []

def backtracking(depth, n):
    # print("backtracking called:", depth, ", n:", n)
    if n == B:
        result.append(depth + 1)
        return

    if n > B:
        return

    backtracking(depth + 1, n * 2)
    backtracking(depth + 1, n * 10 + 1)

backtracking(0, A)

print(min(result) if result else -1)
