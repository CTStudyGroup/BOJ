import sys
input = sys.stdin.readline

# 전위 순회는 노드 위치를 정하는 로직과 동일하다.
pre = []
tree = {}
while True:
    try:
        node = int(input())
        pre.append(node)
        tree[node] = [-1,-1]
    except:
        break

root = pre.pop(0)

for element in pre:
    next = root

    while True:
        if(element < next):
            if(tree[next][0] == -1):
                # 왼쪽이 비어 있다면
                tree[next][0] = element
                break
            else:
                # 왼쪽이 비어있지 않다면
                next = tree[next][0]
        else:
            if(tree[next][1] == -1):
                # 오른쪽이 비어 있다면
                tree[next][1] = element
                break
            else:
                # 오른쪽이 비어있지 않다면
                next = tree[next][1]

# 이제 트리를 후위 순회
# 왼 -> 오 -> 루트

def post(node):
    if(tree[node][0] == -1 and tree[node][1] == -1):
        print(node)
        return

    if(tree[node][0] != -1):
        next = tree[node][0]
        post(next)

    if(tree[node][1] != -1):
        next = tree[node][1]
        post(next)

    print(node)


post(root)