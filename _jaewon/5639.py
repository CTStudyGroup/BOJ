import sys
input_data = list(map(int, sys.stdin.read().split()))

pre = input_data
tree = {node: [-1, -1] for node in pre}

root = pre[0]
for element in pre[1:]:
    cur = root
    while True:
        if element < cur:
            if tree[cur][0] == -1:
                tree[cur][0] = element
                break
            cur = tree[cur][0]
        else:
            if tree[cur][1] == -1:
                tree[cur][1] = element
                break
            cur = tree[cur][1]
            
# 후위 순회 (스택 1개 + 방문 체크)
stack = [(root, False)]
result = []

while stack:
    node, visited = stack.pop()
    if node == -1:
        continue
    if visited:
        result.append(str(node))
    else:
        # 후위: 왼쪽, 오른쪽, 루트
        stack.append((node, True))        # 나중에 출력
        stack.append((tree[node][1], False))  # 오른쪽 먼저 넣어야 왼쪽이 먼저 처리
        stack.append((tree[node][0], False))  # 왼쪽

sys.stdout.write("\n".join(result))
