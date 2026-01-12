import sys

input = sys.stdin.read

def run_stack_machine(commands, start_num):
    stack = [start_num]
    LIMIT = 10**9

    for cmd in commands:
        try:
            if cmd.startswith("NUM"):
                val = int(cmd.split()[1])
                stack.append(val)
            
            elif cmd == "POP":
                if not stack: return "ERROR"
                stack.pop()
                
            elif cmd == "INV":
                if not stack: return "ERROR"
                stack[-1] = -stack[-1]
                
            elif cmd == "DUP":
                if not stack: return "ERROR"
                stack.append(stack[-1])
                
            elif cmd == "SWP":
                if len(stack) < 2: return "ERROR"
                stack[-1], stack[-2] = stack[-2], stack[-1]

            elif cmd == "ADD":
                if len(stack) < 2: return "ERROR"
                a, b = stack.pop(), stack.pop()
                res = b + a
                if abs(res) > LIMIT: return "ERROR"
                stack.append(res)

            elif cmd == "SUB":
                if len(stack) < 2: return "ERROR"
                a, b = stack.pop(), stack.pop()
                res = b - a
                if abs(res) > LIMIT: return "ERROR"
                stack.append(res)

            elif cmd == "MUL":
                if len(stack) < 2: return "ERROR"
                a, b = stack.pop(), stack.pop()
                res = b * a
                if abs(res) > LIMIT: return "ERROR"
                stack.append(res)

            elif cmd == "DIV":
                if len(stack) < 2: return "ERROR"
                a, b = stack.pop(), stack.pop()
                if a == 0: return "ERROR"
                
                res = abs(b) // abs(a)
                if (a < 0 and b > 0) or (a > 0 and b < 0):
                    res = -res
                stack.append(res)

            elif cmd == "MOD":
                if len(stack) < 2: return "ERROR"
                a, b = stack.pop(), stack.pop()
                if a == 0: return "ERROR"
                res = abs(b) % abs(a)
                if b < 0:
                    res = -res
                stack.append(res)
        except:
            return "ERROR"

    if len(stack) == 1:
        return stack[0]
    else:
        return "ERROR"

# --- 메인 실행부 ---
data = input().split()
idx = 0

while idx < len(data):
    if data[idx] == "QUIT":
        break
    
    # 명령어 모으기
    commands = []
    while data[idx] != "END":
        if data[idx] == "NUM":
            commands.append(f"NUM {data[idx+1]}")
            idx += 2
        else:
            commands.append(data[idx])
            idx += 1
    idx += 1
    
    n = int(data[idx])
    idx += 1
    for _ in range(n):
        start_val = int(data[idx])
        idx += 1
        print(run_stack_machine(commands, start_val))
    
    print() # 기계별 구분 빈 줄
