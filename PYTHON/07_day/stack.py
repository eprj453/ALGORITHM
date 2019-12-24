store = [0] * 3 # 저장소
top = -1

def push(item):
    global top
    # full 상태 체크
    if top == 2:
        return 'stack full'
    top += 1
    store[top] = item

def pop(): # 항상 empty 상황을 체크한다.
    global top
    if top == -1:
        return 'stack empty'
    # or
    if len(store) == 0:
        return 'stack empty'

    top -= 1
    return store[top]

def isempty():
    return len(store) == 0