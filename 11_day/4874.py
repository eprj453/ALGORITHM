import sys
sys.stdin = open('4874_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    code = list(input().split())
    # print(code)
    stack = []
    ans = ''
    for ch in code:
        try:
            if ch.isdigit():
                stack.append(int(ch))
            if ch == '+' or ch == '*' or ch == '-' or ch == '/':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if ch == '+':
                    stack.append(int(num2 + num1))
                elif ch == '*':
                    stack.append(int(num2 * num1))
                elif ch == '-':
                    stack.append(int(num2 - num1))
                elif ch == '/':
                    stack.append(int(num2 / num1))
            if ch == '.':
                if len(stack) == 1:
                    ans = stack.pop()
                else:
                    ans = 'error'
        except:
            ans = 'error'
    print('#{} {}'.format(i, ans))