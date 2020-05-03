# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def operation(stk, s):
    if s == 'DUP': stk.append(stk[-1])
    elif s == 'POP': stk.pop()
    else:
        if len(stk) < 2: return []
        else:
            n1, n2 = stk.pop(), stk.pop()
            n2 *= -1 if s == '+' else 1
            if n1 - n2 < 0 : return []
            else: stk.append(n1-n2)
    return stk

def solution(S):
    stk = []
    S = list(S.split(' '))
    for s in S:
        if s.isdigit(): stk.append(int(s))
        else:
            if not stk: return -1
            else: stk = operation(stk, s)
    return stk[-1]

print(solution("13 DUP 1"))