T = int(input())

fibo = []
fibo.append(0)
fibo.append(1)

index = 2
new = 1
while new < 1000000000:
    new = fibo[index-1] + fibo[index-2]
    fibo.append(new)
    index += 1

print(fibo)
print(len(fibo))

for _ in range(T):
    int(input())
