import sys
sys.stdin = open('card_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    s_v, c_v, d_v, h_v = [False] * 14, [False] * 14, [False] * 14, [False] * 14
    s_count, c_count, d_count, h_count = 13, 13, 13, 13
    cards = list(input())
    ans = ''
    for j in range(len(cards)):
        card = ''
        num = 0
        if cards[j].isalpha():
            card, num = cards[j], int(cards[j+1] + cards[j+2])
            if card == 'S':
                if s_v[num] == True:
                    ans = 'ERROR'
                    break
                else:
                    s_v[num] = True
                    s_count -= 1
            elif card == 'C':
                if c_v[num] == True:
                    ans = 'ERROR'
                    break
                else:
                    c_v[num] = True
                    c_count -= 1
            elif card == 'D':
                if d_v[num] == True:
                    ans = 'ERROR'
                    break
                else:
                    d_v[num] = True
                    d_count -= 1
            else:
                if h_v[num] == True:
                    ans = 'ERROR'
                    break
                else:
                    h_v[num] = True
                    h_count -= 1
        else:
            continue

    print('#{} {}'.format(i, 'ERROR')) if ans == 'ERROR' \
        else print('#{} {} {} {} {}'.format(i, s_count, d_count, h_count, c_count))

    # if ans == 'ERROR':
    #     print('#{} {}'.format(i, 'ERROR'))
    # else:
    #     print('#{} {} {} {} {}'.format(i, s_count, d_count, h_count, c_count))


    # print(cards)
