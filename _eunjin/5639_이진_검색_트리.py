import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

N = len(preorder)

# 이진트리를 전위탐색할시에 부모 노드값은 배열[0]
# 부모노드값보다 커지는 숫자가 나올때까지 왼쪽 서브트리 그 이후엔 오른쪽 서브 트리다.
def dfs(start, end):
    if start > end:
        return

    root = preorder[start]
    split = end + 1

    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            split = i  # 오른쪽 서브트리가 시작되는 지점
            break

    # postorder: 왼쪽 -> 오른쪽 -> 루트 순으로 방문
    dfs(start + 1, split - 1)  # 왼쪽
    dfs(split, end)  # 오른쪽
    print(root)

dfs(0, N - 1)
