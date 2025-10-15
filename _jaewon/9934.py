# 입력값: 중위 순회의 결과
# 중위 순회의 결과로 원본 트리를 구하라.

levels = int(input().strip())
buildings = list(map(int, input().split()))

tree = [[-1,-1,0] for _ in range(2**levels)]
tree[1] = [2,3,0] # 왼쪽 자식 노드 번호, 오른쪽 자식 노드 번호, 실제 빌딩 넘버

for i in range(2, 2**(levels-1)):
    tree[i] = [i*2, i*2+1, 0]

# 중위 순회
building_index = 0

def mid(node):
    global building_index
    if(tree[node][0] == -1 and tree[node][1] == -1):
        tree[node][2] = buildings[building_index]
        building_index += 1
        return
    
    # 왼쪽 탐색
    mid(tree[node][0])

    # 중앙 탐색
    tree[node][2] = buildings[building_index]
    building_index += 1

    # 오른쪽 탐색
    mid(tree[node][1])

mid(1)
index = 1
for level in range(levels):
    tmp = []
    for _ in range(2**level):
        tmp.append(tree[index][2])
        index+=1
    print(*tmp)    
