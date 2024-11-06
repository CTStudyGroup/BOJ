# 입력 받기
N = int(input())

arr = []

for _ in range(N):
    text = input()
    if not text in arr:
        arr.append(text)

result = sorted(arr, key=lambda x: (len(x), x))

# print(arr)
# print(result)

print('\n'.join(result))
