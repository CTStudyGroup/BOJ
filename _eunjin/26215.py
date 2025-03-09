N = int(input())
snow = list(map(int, input().split()))

snow.sort(reverse=True)

answer = 0

for i in range(N):
    while snow[i] > 0:
        for j in range(i + 1, N):
            while snow[i] > 0 and snow[j] > 0:
                snow[i] -= 1
                snow[j] -= 1
                answer += 1
                print(snow)
                print("answer:", answer)
        if snow[i] <= 0:
            break
        snow[i] -= 1
        answer += 1
        print("-- outside --")
        print(snow)
        print("answer:", answer)


print(answer if answer <= 1440 else -1)
