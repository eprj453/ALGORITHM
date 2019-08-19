# import sys
# sys.stdin = open('4866_input.txt', 'r')


t = int(input())
for i in range(1, t+1):
    result = 1
    store = []
    sentence = input()
    # print(len(sentence))
    for letter in sentence:
        if letter == '(' or letter == '{':
            store.append(letter)
            # print(store)
        if letter == ')':
            # print(') 만남')
            if len(store) == 0:
                result = 0
                break
            if store.pop() != '(':
                # print('store.pop() : {}'.format(store.pop()))
                result = 0
                break
            # print(store)

        if letter == '}':
            # print('} 만남')
            if len(store) == 0:
                result = 0
                break
            if store.pop() != '{':
                result = 0
                break
            # print(store)

    # print('final : {}'.format(store))
    if len(store) != 0:
        result = 0

    print('#{} {}'.format(i, result))

# print('#{} {)}'.format(tc, find())
# {}{}{{{{(((()))}}}}
# }{)}