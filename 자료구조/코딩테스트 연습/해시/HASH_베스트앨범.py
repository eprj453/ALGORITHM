def solution(genres, plays):
    answer = []
    music_dict = {}
    music_dict_reverse = {}
    play_dict = {}

    for k in range(len(genres)):
        music_dict[genres[k]] = music_dict.get(genres[k], 0) + plays[k]
        play_dict[genres[k]] = play_dict.get(genres[k], []) + [[plays[k], 10000-k]]

    for key, values in music_dict.items():
        music_dict_reverse[values] = key

    total_list = sorted(list(music_dict.values()), reverse = True)

    for total in total_list:
        key = music_dict_reverse[total]
        genre_total_list = sorted(play_dict[key], reverse = True)
        n = 0
        end = 2 if len(genre_total_list) > 1 else 1
        while n < end:
            answer.append(10000 - genre_total_list[n][1])
            n += 1

    return answer


    # print(sorted(list(music_dict.values()), reverse=True))
solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])