# Least Frequently Used
limit = int(input())
thumbs = int(input())
toward = list(map(lambda x: x-1, map(int, input().split())))

thumbs_count = [0 for _ in range(101)]  # 추천 수를 저장
frames = []  # 게시한 순서대로 학생번호를 저장

for student in toward:
    if student in frames:
        # 이미 액자에 있는 학생이라면 추천 수만 증가
        thumbs_count[student] += 1
        continue
    
    # 새로운 학생이라면
    if len(frames) == limit:
        # 현재 액자에 있는 학생들의 추천 수 중 최솟값 찾기
        min_thumbs = min(thumbs_count[student] for student in frames)
        
        # 추천 수가 최소인 학생 중, 가장 먼저 들어온 학생 제거
        for i in range(len(frames)):
            if thumbs_count[frames[i]] == min_thumbs:
                removed_student = frames.pop(i)
                thumbs_count[removed_student] = 0
                break
    
    # 새 학생 추가
    frames.append(student)
    thumbs_count[student] += 1

# 결과 출력 (1-indexed로 변환 후 정렬)
frames = list(map(lambda x: x+1, frames))
print(sorted(frames))