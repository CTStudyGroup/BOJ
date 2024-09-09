# 입력 받기
N = int(input())

# 각 선수의 등번호, 곱한 점수, 합산 점수 저장하기 위함
num_arr = []
mul_dict = {}
sum_dict = {}

for _ in range(N):
    num, p, q, r = map(int, input().split())

    # 각 선수의 등번호, 곱한 점수, 합산 점수 저장
    num_arr.append(num)
    mul_dict[num] = p*q*r
    sum_dict[num] = p+q+r

# num_arr을 정렬하는데, 이때 기준은 1.곱한 점수 오름차순 2.합산점수 오름차순 3.등번호 오름차순
top3 = sorted(num_arr, key=lambda x: (mul_dict[x], sum_dict[x], x))[:3]

for elem in top3:
    print(elem, end=" ")
