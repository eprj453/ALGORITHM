expression = '(6+5*(2-8)/2)'

stack = []

in_prior = [['+', 1], ['-', 1], ['*', 2], ['/', 2], ['(', 0], [')', 3]]

for token in expression:
    if token.isdigit(): # 숫자라면
        # print('stack : {}'.format(stack))
        print(token, end = ' ')

    else: # 숫자가 아니라 문자라면
        # print('stack : {}'.format(stack))
        if token == '(': # 여는 괄호라면
            stack.append(token)
            # print(stack)
        elif token == ')': # 닫는 괄호라면
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    print(stack.pop(), end=' ')

        else: # 연산자라면
            num = 0 # 현재 연산자의 우선순위
            for prior in in_prior:
                if token == prior[0]:
                    num = prior[1] # 내 연산자 우선순위
                    break
            while True:
                stack_num = 0
                if len(stack) == 0:
                    stack.append(token)
                    break
                for prior in in_prior:
                    if stack[-1] == prior[0]:
                        stack_num = prior[1]  # in stack 연산자
                        break
                if num > stack_num: # 내 연산자의 우선순위가 더 높다면
                    stack.append(token)
                    break
                else:
                    print(stack.pop(), end = ' ')



