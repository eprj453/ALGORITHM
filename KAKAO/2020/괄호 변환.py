
def myfunc(string, answer):
    # print('호출')
    # global answer
    # print(ans)
    left, right, cut = 0, 0, 0
    u, v = '', ''
    for i in range(0, len(string)):
        if string[i] == '(':
            left += 1
        elif string[i] == ')':
            right += 1

        if left != 0 and right != 0 and left == right:
            cut = i
            break

    u, v = string[0:cut+1], string[cut+1:len(string)]
    if u == '':
        return
    # print("u : {}, v : {}".format(u, v))
    l, r = (len(u)//2)-1, len(u)//2
    isRight = True
    stk = []
    for j in range(0, len(u)):
        if u[0] == ')':
            isRight = False
            break

        if u[j] == '(':
            stk.append(u[j])
        elif u[j] == ')':
            if len(stk) == 0:
                isRight = False
                break
            else:
                stk.pop()

    if isRight:
        answer += u
        myfunc(v, answer)
    else:
        answer += '('
        myfunc(v, answer)
        answer += ')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            elif u[i] == ')':
                answer += '('

def solution(p):
    answer = myfunc(p, '')
    return answer


solution('()))((()')