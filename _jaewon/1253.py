# 40000개의 해시를 만들어 놓고 계산
# 수의 위치가 다르면 값이 같아도 다른 수이다.

n = int(input())

hash_map = {}
numbers = list(map(int, input().split()))
numbers.sort()
count = 0

for index in range(n):
    target = numbers[index]
    start = 0
    end = n-1

    while start < end:
        if(numbers[start] + numbers[end] == target):
            if(start == index):
                start += 1
            elif(end == index):
                end -= 1
            else:
                count += 1
                break
        elif(numbers[start] + numbers[end] > target):
            end -= 1
        else:
            start += 1

print(count)