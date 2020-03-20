t = int(input())
for x in range(1, t+1):
    n = int(input())
    card = input()
    card_list = []
    for i in card:
        card_list.append(int(i))
    #print('카드 리스트는 {}'.format(card_list))
    max_card = max(card_list)
    #print('최대값은 {}'.format(max_card))
    check_list = [0] * (max_card+1)

    for j in card_list:
        check_list[j] += 1
    print(check_list)

    max_val = 0
    max_index = 0

    for k in range(0, len(check_list)):
        if check_list[k] >= max_val:
            max_val = check_list[k]
            max_index = k
    print('#{} {} {}'.format(x, max_index, max_val))




