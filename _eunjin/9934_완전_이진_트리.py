K = int(input())
arr = list(map(int, input().split()))

# 주어진 arr의 가운데 = root
# arr 왼쪽 부분 = 왼쪽 서브트리
# arr 오른쪽 부분 = 오른쪽 서브트리
# 서브트리 안에서의 가운데 = 그 서브트리의 root
# 서브트리로 좁혀갈 떄마다 depth +1

answer = [[] for _ in range(K)]

def recursion(start, end, depth):
    if start == end:
        answer[depth].append(arr[start])
        return

    root = (start + end) // 2
    recursion(start, root - 1, depth + 1)
    answer[depth].append(arr[root])
    recursion(root + 1, end, depth + 1)

recursion(0, len(arr) - 1, 0)

for row in answer:
    print(' '.join(map(str, row)))
