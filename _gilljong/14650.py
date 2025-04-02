from sys import stdin as s
s = open("txt/14650.txt", "r")

N = int(s.readline())

answer = 0
def dfs(c, value): # dfs를 통해 자릿수만큼 숫자 생성
    global answer
    if c == N-1: # 자릿수에 도달 시
        if int(value) % 3 == 0: # 3의 배수 체크
            answer += 1
        return
    for i in range(3):
        dfs(c+1, value + str(i)) # 시작 수 제외 0,1,2 재귀

for i in range(1,3): # 시작 수를 1, 2로 고정 후 N-1 만큼 반복
    dfs(0,str(i))

print(answer)

#19m 29s