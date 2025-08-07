# 팀이 될 수 있는 경우 -> 사이클이 만들어지는 경우
# 자기 자신을 선택하더라도 사이클이 만들어 질 수 있다.
# 연결리스트와 status 배열 사용

# 만약 연결리스트의 노드를 모두 순회하고 head로 돌아오면 성공
# 모든 노드를 head로 설정하고 한번씩 순회

# status: 0 -> 초기 상태, 아직 한번도 순회되지 않음
# status: 1 -> 이 노드를 통과하는 모든 경로는 실패, 즉 팀을 이룰 수 없음
# status: 2 -> 팀을 이룬 상태

T = int(input())

for case in range(T):
    # 초기 설정 ==============
    n = int(input())

    toward = list(map(int,input().split(' '))) # 선택 번호 배열
    toward = list(map(lambda x: x-1, toward)) # index 0으로 맞추기 위해 1씩 뺌
    status = [0] * n # 각 학생의 상태 배열

    for number, index in enumerate(toward, 0):
        if (number == index):
            status[index] = 2

    # 각 노드 순회 ==============
    for node in range(n):
        # node가 초기 상태가 아니면 순회할 필요 없음
        if(status[node] != 0):
            continue

        elements = []
        while(True):
            if(status[node] == -1):
                # 사이클 발견
                cycle_start = elements.index(node)
                for i in range(len(elements)):
                    if i >= cycle_start:
                        status[elements[i]] = 2  # 팀 결성
                    else:
                        status[elements[i]] = 1  # 실패
                break
            elif(status[node] != 0):
                # 이미 방문 완료된 노드
                for x in elements:
                    status[x] = 1
                break
            else:
                elements.append(node)
                status[node] = -1  # 방문 중
                node = toward[node]
    print(status.count(1))


