import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

h_arr = []
for idx, a in enumerate(arr):
    heapq.heappush(h_arr, (a, idx))

M = int(input())
for _ in range(M):
    t = input().split()
    if t[0] == "2":
        while h_arr:
            num, idx = heapq.heappop(h_arr)
            if arr[idx] == num:   # 최신 값인지 확인
                print(idx+1)
                heapq.heappush(h_arr, (num, idx))  # 다시 넣기
                break
    else:  # "1 i v"
        idx, new_num = int(t[1]) - 1, int(t[2])
        arr[idx] = new_num
        heapq.heappush(h_arr, (new_num, idx))
