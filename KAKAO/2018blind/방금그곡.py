def get_minute(start, end):
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    return (end_h * 60 + end_m) - (start_h * 60 + start_m)


def get_full_melody(melody, time):
    full_melody = []

    i = 0
    while i < time:
        idx = i % len(melody)
        full_melody.append(melody[idx])
        i += 1

    return full_melody


def solution(m, musicinfos):
    answer, play_time = '(None)', 0
    m += ' '
    m_list = []
    for idx, ch in enumerate(m):
        if ch == '#' or ch == ' ': continue
        m_list.append(ch + '#' if m[idx + 1] == '#' else ch)

    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        minute = get_minute(start, end)
        melody += ' '
        melody_list = []
        for idx, ch in enumerate(melody):
            if ch == '#' or ch == ' ': continue
            melody_list.append(ch + '#' if melody[idx + 1] == '#' else ch)

        full_melody = get_full_melody(melody_list, minute)

        len_m = len(m_list)

        i = 0
        while i <= len(full_melody):
            if m_list == full_melody[i: i + len_m]:
                if play_time < minute:
                    answer, play_time = title, minute
            i += 1

    return answer