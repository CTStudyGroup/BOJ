A, B = input().split()

# n자리 순열 만들어지면 숫자로 변환해서 B보다 작으면 answer 갱신
A = list(A)
B = int(B)

def bt(n):
    global arr, answer
    if n == len(A):
        if arr[0] == '0':  # 0으로 시작하는건 고려X
            return
        st = ''.join(arr)
        num = int(st)
        if num < B:
            answer = max(answer, num)
        return

    for i in range(len(A)):
        if not visited[i]:
            visited[i] = True
            arr.append(A[i])
            bt(n + 1)
            arr.pop()
            visited[i] = False


answer = -1
arr = []
visited = [False] * (len(A))
bt(0)
print(answer)
