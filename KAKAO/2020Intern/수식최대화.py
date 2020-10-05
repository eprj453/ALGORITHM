from itertools import permutations

def make_postfix(expression, rank):

    ope_stack, answer = [], []
    for ex in expression:
        if ex.isdecimal():
            answer.append(ex)
        else:
            if not ope_stack:
                ope_stack.append(ex)
            else:
                while ope_stack:
                    cmp, stk = rank.get(ex), rank.get(ope_stack[-1])
                    if cmp > stk:
                        break
                    answer.append(ope_stack.pop())
                ope_stack.append(ex)

    while ope_stack:
        answer.append(ope_stack.pop())

    return answer

def make_list(expression):
    answer = []
    num = ''
    for idx, ex in enumerate(expression):
        if not ex.isdecimal():
            answer.append(num)
            answer.append(ex)
            num = ''
        else:
            num += ex

    answer.append(num)
    return answer

def calculate_postfix(expression):
    stk = []
    for ex in expression:
        if ex.isdecimal():
            stk.append(ex)
        else:
            num_1, num_2 = int(stk.pop()), int(stk.pop())
            if ex == '+':
                stk.append(num_1 + num_2)
            elif ex == '*':
                stk.append(num_1 * num_2)
            else:
                stk.append(num_2 - num_1)
    return stk

def solution(expression):
    answer = 0
    expression_list = make_list(expression)
    operations = ['*', '+', '-']
    for arr in permutations(operations):
        rank = {value: idx for idx, value in enumerate(arr)}
        postfix = make_postfix(expression_list, rank)

        result = calculate_postfix(postfix)
        if result:
            answer = max(answer, abs(result[-1]))
    return answer

print(solution("100-200*300-500+20"))
