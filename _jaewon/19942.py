import sys
input = sys.stdin.readline

N = int(input())
limit = list(map(int, input().split()))

food = [] 
for _ in range(N):
    food.append(list(map(int, input().split())))

def sum_attrs(array1, array2, array3):
    total = []
    for i in range(5):
        total.append(array1[i] + array2[i] + array3[i])
    return total

minimum = float('inf')
result = None

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            protein, fat, carbon, vita, price = sum_attrs(food[i], food[j], food[k])
            if (protein >= limit[0] and fat >= limit[1] and
                carbon >= limit[2] and vita >= limit[3]):
                
                if price < minimum:
                    minimum = price
                    result = (i+1, j+1, k+1)

if result:
    print(minimum)
    print(*result)
else:
    print(-1)
