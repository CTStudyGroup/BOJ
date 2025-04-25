from collections import deque
import sys
input = sys.stdin.readline

INF = 10**9
# 13 div -4 = -3
# -13 mod 4 = -1
# 13 mod -4 = 1
# -13 mod -4 = -1

def div(n2, n1):  # valid, 결과
    if n2 == 0:
        return False, 0
    if n1 == 0:
        return True, 0

    if (n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0):
        return True, abs(n1) // abs(n2) * (-1)
    else:
        return True, abs(n1) // abs(n2)


def mod(n2, n1):  # valid, 결과
    if n2 == 0:
        return False, 0
    if n1 == 0:
        return True, 0

    if n1 > 0 and n2 > 0:  # 둘다 양수
        return True, n1 % n2
    elif n1 > 0 and n2 < 0:  # 피제수가 음수
        return True, n1 % abs(n2)
    elif n1 < 0 and n2 > 0:  # 제수가 음수
        return True, abs(n1) % n2 * (-1)
    else:  # 둘다 음수
        return True, abs(n1) % abs(n2) * (-1)


def execute(st):
    global stack
    c = list(st.split())
    if c[0] == "NUM":
        stack.append(int(c[1]))
        return True

    cmd = c[0]

    if not stack:  # 숫자가 없으므로 수행 불가
        return False

    if cmd == "POP":
        stack.pop()
        return True
    elif cmd == "INV":
        temp = -stack.pop()
        stack.append(temp)
        return True
    elif cmd == "DUP":
        stack.append(stack[-1])
        return True

    if len(stack) < 2:  # 숫자가 2개보다 적으므로 수행 불가
        return False

    n1 = stack.pop()
    n2 = stack.pop()

    if cmd == "SWP":
        stack.append(n1)
        stack.append(n2)
        return True
    elif cmd == "ADD":
        if abs(n1 + n2) > INF:
            return False
        stack.append(n1 + n2)
        return True
    elif cmd == "SUB":
        if abs(n2 - n1) > INF:
            return False
        stack.append(n2 - n1)
        return True
    elif cmd == "MUL":
        if abs(n1 * n2) > INF:
            return False
        stack.append(n1 * n2)
        return True
    elif cmd == "DIV":
        valid, result = div(n1, n2)
        if not valid:
            return False
        stack.append(result)
        return True
    elif cmd == "MOD":
        valid, result = mod(n1, n2)
        if not valid:
            return False
        stack.append(result)
        return True

command = []
answer = []

while True:
    st = input().strip()
    if st == "QUIT":
        break
    if not st:
        command = []
    elif st == "END":  # 프로그램 명령어 입력 종료, 숫자 받아서 실행
        # print("cmd:", cmd)
        N = int(input())
        ans = []
        for _ in range(N):  # 매 입력 값마다 프로그램 수행
            stack = []
            num = int(input())
            stack.append(num)
            valid = True
            for c in command:
                if not execute(c):
                    valid = False
                    break
            if valid and len(stack) == 1:
                ans.append(stack[0])
            else:
                ans.append("ERROR")
        answer.append(ans)

    else:  # 프로그램 명령어 입력
        command.append(st)

print('\n\n'.join('\n'.join(map(str, elem)) for elem in answer))
