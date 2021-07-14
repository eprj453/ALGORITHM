direction_dirs = {
    1: (0, 1),
    2: (0, -1),
    3: (1, 0),
    4: (-1, 0)
}

swipe_start_line_dirs = {
    1: (1, 0),
    2: (1, 0),
    3: (0, 1),
    4: (0, 1)
}

corner_index = {
    1: (0, 2),
    2: (1, 3),
    3: (0, 1),
    4: (2, 3)
}


def mediate_coop(coop):
    def minus_one(x):
        return x - 1
    return list(map(minus_one, coop))


def get_corners(start, end):
    left_up, right_up, left_down, right_down = start, [start[0], end[1]], [end[0], start[1]], end
    return [left_up, right_up, left_down, right_down]


def slide_window(arr, start, end, d):
    start, end = mediate_coop(start), mediate_coop(end)
    corners = get_corners(start, end)
    c_idx = corner_index[d]
    line_start, line_end = corners[c_idx[0]], corners[c_idx[1]]
    # print(f'linestart : {line_start} / lineend : {line_end}')
    start_lines = get_line(line_start, line_start, line_end, d, swipe_start_line_dirs)

    for start_line in start_lines:
        swipe_line = get_line(start_line, start, end, d, direction_dirs)
        arr = swipe(arr, swipe_line)

    return arr


def get_line(line_start, start, end, d, dictionary):
    line = []
    direction = dictionary[d]
    line_x, line_y = line_start
    start_x, start_y = start
    end_x, end_y = end
    while start_x <= line_x <= end_x and start_y <= line_y <= end_y:
        line.append([line_x, line_y])
        line_x += direction[0]
        line_y += direction[1]
    return line


def swipe(arr, swipe_line):
    last_value = arr[swipe_line[-1][0]][swipe_line[-1][1]]
    for i in range(len(swipe_line)-1, 0, -1):
        now_x, now_y = swipe_line[i]
        prev_x, prev_y = swipe_line[i-1]
        arr[now_x][now_y] = arr[prev_x][prev_y]
    arr[swipe_line[0][0]][swipe_line[0][1]] = last_value
    return arr

'''
dirs = {
    1: (0, 1),
    2: (0, -1),
    3: (1, 0),
    4: (-1, 0)
}

arr = [
    [1, 2, 3],  # 00 01 02
    [4, 5, 6],  # 10 11 12
    [7, 8, 9],  # 20 21 22
    [10, 11, 12]  # 30 31 32
]



[1, 2, 3]
[4, 11, 12]
[7, 5, 6]
[10, 8, 9]

[1, 2, 3]
[4, 8, 9]
[7, 11, 12]
[10, 5, 6]


[1, 2, 3]
[4, 6, 5]
[7, 9, 8]
[10, 12, 11]
'''

example_arr = [
    [1, 2, 3],  # 00 01 02
    [4, 5, 6],  # 10 11 12
    [7, 8, 9],  # 20 21 22
    [10, 11, 12]  # 30 31 32
]

print(slide_window(example_arr, [2, 1], [4, 3], 2))
