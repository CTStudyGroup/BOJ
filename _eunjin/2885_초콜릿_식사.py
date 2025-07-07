K = int(input())

# 6
# ㅁㅁㅁㅁ/ㅁㅁㅁㅁ
# ㅁㅁ/ㅁㅁ/ㅁㅁㅁㅁ

size = 1
count = 0
while size < K:
    size = size * 2

min_size = size

while K > 0:
    if K >= size:
        K -= size
    else:
        size //= 2
        count += 1

print(min_size, count)
