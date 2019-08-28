t = int(input())
for i in range(1, t+1):
    code = list(input().split())
    stack = []
    ans = 0
    # print(code)
    # stack.append(int(code[0]))
    # while len(stack) > 0:
    for ch in code:
        if ch.isdigit():
            stack.append(ch)
        if not stack:
            print('#{} {}'.format(i, 'error'))
            break
        elif ch == '+' or ch == '*' or ch == '-' or ch == '/': # 연산자라면 stack에서 2개 뺀다.
            num1 = stack.pop()
            num2 = stack.pop()
            if ch == '+':
                stack.append(int(num1) + int(num2))
                ans = (int(num2) + int(num1))
            elif ch == '*':
                stack.append(int(num1) * int(num2))
                ans = (int(num2) * int(num1))
            elif ch == '-':
                stack.append(int(num1) - int(num2))
                ans = (int(num2) - int(num1))
            elif ch == '/':
                stack.append(int(num1) / int(num2))
                ans = (int(num2) / int(num1))
        elif ch == '.':
            print('#{} {}'.format(i, int(ans)))
            break