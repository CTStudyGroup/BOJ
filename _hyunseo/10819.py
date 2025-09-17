from collections import deque

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr = deque(arr)

# N이 홀수인 경우, 가장 중앙에 올 숫자를 정하기 위한 flag
flag = 0 if abs(arr[0]-arr[1]) > abs(arr[-1] - arr[-2]) else 1

# 새로운 배열을 저장할 new_arr
new_arr = deque()


def solve(arr, flag) :
  """ 주어진 배열과 flag을 사용해서, 최대차이를 만드는 배열을 생성하고, 최대 차이를 구해서 반환"""
    tmp = 0
    if flag == 0 :
        while arr :
            if tmp %2 == 0 :
                new_arr.appendleft(arr.pop())
                if arr :
                    new_arr.append(arr.popleft())
            else :
                new_arr.append(arr.pop())
                if arr :
                    new_arr.appendleft(arr.popleft())
            tmp += 1
    else :
        while arr :
            if tmp %2 == 0 :
                new_arr.appendleft(arr.popleft())
                if arr :
                    new_arr.append(arr.pop())
            else :
                new_arr.append(arr.popleft())
                if arr :
                    new_arr.appendleft(arr.pop())
            tmp += 1
    
    
    # -- 답 구하기 --
    answer = 0 
    for i in range(len(new_arr)-1) :
        answer += abs( new_arr[i] - new_arr[i+1])
    return answer


print(solve(arr, flag))
