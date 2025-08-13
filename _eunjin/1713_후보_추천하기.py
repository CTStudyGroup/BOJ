import sys
input = sys.stdin.readline

N = int(input())
R = int(input())
recommend = list(map(int, input().split()))

# 우선순위큐로 하려고 했으나.. 큐의 특정 인덱스의 값을 수정해야하는데 heapq에서는 불가
# 딕셔너리에 {학생 번호: [추천 횟수, 게시 시점]} 이렇게 저장하고 완전탐색할까
# N이 20, 추천 횟수 1,000이라 N*R 가능

_dict = {}

# 삭제할 학생 번호 리턴
# 1. 추천횟수 적은순, 2. 게시 시점 오래된 순
def get_min():
    mn = 1001
    mn_students = []
    for key, value in _dict.items():
        if value[0] == mn:
            mn_students.append(key)
        elif value[0] < mn:
            mn_students = [key]
            mn = value[0]

    ret = -1
    oldest = R
    for st in mn_students:
        if _dict[st][1] < oldest:
            ret = st
            oldest = _dict[st][1]

    return ret

for i in range(R):
    student = recommend[i]

    if student in _dict:  # 이미 학생의 사진이 게시된 경우
        _dict[student][0] += 1  # 추천 횟수 증가
    else:
        if len(_dict) >= N:  # 비어있는 사진틀 없는 경우
            mn_student = get_min()
            del _dict[mn_student]  # 해당 학생 사진틀에서 제거

        _dict[student] = [1, i]

print(*sorted(_dict.keys()))
