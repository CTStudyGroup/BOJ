N = int(input())

arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if arr[i-1] > arr[i]:
        print("arr[i-1]:", arr[i-1], ", arr[i]:", arr[i])
        for j in range(N-1, 0, -1):
            if arr[i-1] > arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                temp_arr = sorted(arr[i:], reverse=True)
                arr = arr[:i]+temp_arr
                print(' '.join(map(str, arr)))
                exit()

print(-1)
