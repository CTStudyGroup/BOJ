from itertools import combinations

# 입력 받기
L, C = map(int, input().split())
arr = list(input().split())

# 최소 한개의 모음, 두개의 자음이라는 조건
# 암호 후보가 될 문자를 모두 뽑은 후, 정렬해서 출력하기

# 모음, 자음 각각 추출
vowels = ['a', 'e', 'i', 'o', 'u']

mo = []
ja = []
for c in arr:
    if c in vowels:
        mo.append(c)
    else:
        ja.append(c)


# 자음 후보 리스트 생성
ja_comb = list(combinations(ja, 2))

# 최종 암호 문자열 리스트
result = []

for m in range(len(mo)):
    for j in range(len(ja_comb)):
        picked = []

        # 모음 리스트에서 일단 1개 뽑기
        picked.append(mo[m])

        # 자음 후보 리스트에서 일단 2개 뽑기
        picked.append(ja_comb[j][0])
        picked.append(ja_comb[j][1])

        # 나머지 문자 후보 리스트 생성
        other = arr[:]
        other.remove(mo[m])
        other.remove(ja_comb[j][0])
        other.remove(ja_comb[j][1])

        # 나머지 모음+자음에서 남은 개수만큼 뽑기
        other_comb = list(combinations(other, L-3))
        for elem in other_comb:
            # 최종 선택된 문자 리스트 생성
            final_picked = picked+list(elem)

            # 암호는 알파벳순이므로 정렬
            final_picked.sort()

            # 암호 리스트를 하나의 문자열로 합치기
            total = ''.join(final_picked)

            # 최종 암호 리스트에 없는 경우에만 추가
            if total not in result:
                result.append(total)


result.sort()
for elem in result:
    print(elem)


# 다른 풀이
# 모든 가능한 조합 다 뽑고 거기서 최소 1개의 모음, 2개의 자음이 없는 애들은 거르기
# all_list = list(combinations(sorted(arr), L))
# result = []
# for elem in all_list:
#     # 모음 개수와 자음 개수 세기
#     vowel_count = 0
#     consonant_count = 0
#     for char in elem:
#         if char in "aeiou":
#             vowel_count += 1
#         else:
#             consonant_count += 1

#     # 모음이 최소 1개, 자음이 최소 2개인 경우만 처리
#     if vowel_count >= 1 and consonant_count >= 2:
#         print(''.join(elem))
