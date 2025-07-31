S, N = input().split()
S = int(S)
N = list(N)
W = S + 2
H = 2 * S + 3

# -- 가로선을 arr에 추가
def hor(arr):
    arr.append(' ' + '-' * S + ' ' + ' ')

# | 세로선을 arr에 추가, 오른쪽 1줄
def ver1(arr):
    for _ in range(S):
        arr.append(' ' * (W - 1) + '|' + ' ')

# | 세로선을 arr에 추가, 왼쪽 1줄
def ver2(arr):
    for _ in range(S):
        arr.append('|' + ' ' * (W - 1) + ' ')

# | 세로선을 arr에 추가, 양쪽 1줄씩
def ver3(arr):
    for _ in range(S):
        arr.append('|' + ' ' * (W - 2) + '|' + ' ')

def blank(arr):
    arr.append(' ' * W + ' ')

nums = []

arr0 = []  # 0
hor(arr0)
ver3(arr0)
blank(arr0)
ver3(arr0)
hor(arr0)
nums.append(arr0)

arr1 = []
blank(arr1)
ver1(arr1)
blank(arr1)
ver1(arr1)
blank(arr1)
nums.append(arr1)

arr2 = []
hor(arr2)
ver1(arr2)
hor(arr2)
ver2(arr2)
hor(arr2)
nums.append(arr2)

arr3 = []
hor(arr3)
ver1(arr3)
hor(arr3)
ver1(arr3)
hor(arr3)
nums.append(arr3)

arr4 = []
blank(arr4)
ver3(arr4)
hor(arr4)
ver1(arr4)
blank(arr4)
nums.append(arr4)

arr5 = []
hor(arr5)
ver2(arr5)
hor(arr5)
ver1(arr5)
hor(arr5)
nums.append(arr5)

arr6 = []
hor(arr6)
ver2(arr6)
hor(arr6)
ver3(arr6)
hor(arr6)
nums.append(arr6)

arr7 = []
hor(arr7)
ver1(arr7)
blank(arr7)
ver1(arr7)
blank(arr7)
nums.append(arr7)

arr8 = []
hor(arr8)
ver3(arr8)
hor(arr8)
ver3(arr8)
hor(arr8)
nums.append(arr8)

arr9 = []
hor(arr9)
ver3(arr9)
hor(arr9)
ver1(arr9)
hor(arr9)
nums.append(arr9)


answer = ['' for _ in range(H)]
for n in N:
    n = int(n)
    num = nums[n]
    for h in range(H):
        answer[h] += num[h]

print('\n'.join(answer))
