import sys
input = sys.stdin.readline

# 땅 개수 N, 오리 수 Q
N, Q = map(int, input().split())
# 주인있는 땅 표시 (있으면 1, 없으면 0)
ownership = [0] * (N + 1)


for _ in range(Q) :
    duck_wants =int(input())  # 원하는 땅
    parents = []  #  부모 노드 저장 배열
    tmp = duck_wants  # 부모 노드 찾기 위한 임시 변수
    parents_all = 0  # 부모 노드가 다 0인 경우 찾기 위한 변수
    while tmp != 1 :
        tmp //= 2
        parents_all += ownership[tmp]
        parents.append(tmp)
    
    # parents_all는 모든 부모가 땅이 없는 경우
    if parents_all == 0 :
        if ownership[duck_wants] == 0 :
            print(0)
            ownership[duck_wants] = 1
        else :  # 원하는 땅이 이미 차지된 경우
            print(duck_wants)
    else :  # 부모 노드 중에서 차지된 땅이 있는 경우
        for parent in parents[::-1] :
            if ownership[parent] == 1 :
                print(parent)
                break

    
