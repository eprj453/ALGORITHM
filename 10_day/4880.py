def game(game_list, game_list2):
    global g_list
    if len(game_list) == 2 and len(game_list2) == 2:
        if game_list[0] == 1 and game_list2[0] == 3:
            return game_list
        elif game_list[0] == 1 and game_list2[0] == 2:
            return game_list2
        elif game_list[0] == 2 and game_list2[0] == 3:
            return game_list2
        elif game_list[0] == 2 and game_list2[0] == 1:
            return game_list
        elif game_list[0] == 3 and game_list2[0] == 1:
            return game_list
        elif game_list[0] == 3 and game_list2[2] == 2:
            return game_list2
        else:
            return game_list
    else:
        game(g_list[0:(0+)])