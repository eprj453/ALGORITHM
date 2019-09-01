def game(game_list, game_list2):
    n, n2 = len(game_list), len(game_list2)
    print(game_list, game_list2)
    if len(game_list) == 1 and len(game_list2) == 1:
        print('함수 작동')
        print('비교 :  {}, {}'.format(game_list, game_list2))
        if game_list[0][0] == '1' and game_list2[0][0] == '3':
            print('당첨, return', game_list)
            return game_list
        elif game_list[0][0] == '1' and game_list2[0][0] == '2':
            print('당첨, return', game_list2)
            return game_list2
        elif game_list[0][0] == '2' and game_list2[0][0] == '3':
            print('당첨, return', game_list2)
            return game_list2
        elif game_list[0][0] == '2' and game_list2[0][0] == '1':
            print('당첨, return', game_list)
            return game_list
        elif game_list[0][0] == '3' and game_list2[0][0] == '1':
            print('당첨, return', game_list2)
            return game_list
        elif game_list[0][0] == '3' and game_list2[0][0] == '2':
            print('당첨, return', game_list2)
            return game_list2
        else:
            print('당첨, return', game_list)
            return game_list
    else:
        if n % 2 == 1:
           return game(game_list[:(n // 2) + 1], game_list[(n // 2) + 1:])
        else:
            return game(game_list[:(n // 2)], game_list[(n // 2):])

        if n2 % 2 == 1:
            return game(game_list2[:(n2 // 2) + 1], game_list2[(n2 // 2) + 1:])
        else:
           return game(game_list2[:(n2 // 2)], game_list2[(n2 // 2):])


cards = [['1', 1], ['3', 2], ['3', 3], ['3', 4], ['1', 5], ['1', 6], ['3', 7]]

n = len(cards)

if n % 2 == 1:  # 홀수라면
    print(game(cards[:(n // 2) + 1], cards[(n // 2) + 1:]))
else:
    print(game(cards[:n // 2], cards[n // 2:]))