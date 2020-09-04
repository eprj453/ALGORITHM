def can_rotate(board, location):
    pass

def can_move(board, present, direction):
    n = len(board)
    x, y = present[0], present[1]
    dx, dy = direction[0], direction[1]
    if 0 <= x+dx < n and 0 <= y+dy < n and not board[x+dx][y+dy]:
        return [x + dx, y + dy]
    return None




def solution(board):
    n = len(board)
    dist_dict = {}
    move_dirs = [(0, 1), (0, -1), (1, 0),(-1, 0)]
    first_rotate_dirs = [[[1, 0], [0, -1]], [[-1, 0], [0, -1]]]
    second_rotate_dirs = [[[-1, 0], [0, 1]], [[1, 0], [0, 1]]]

    for i in range(n):
        for j in range(n-1):
            if 0 <= i < n and 0 <= j < n:
                dist_dict[((i, j), (i, j+1))] = 0xffffff
    for i in range(n-1):
        for j in range(n):
            if 0 <= i < n and 0 <= j < n:
                dist_dict[((i, j), (i+1, j))] = 0xffffff

    dist_dict[((0, 0), (0, 1))] = 0
    robot = [((0, 0), (0, 1))]

    while robot:
        axis_first, axis_second = robot.pop(0)
        dist = dist_dict[(axis_first, axis_second)]
        for d in move_dirs:
            next_x, next_y = can_move(board, axis_first, d), can_move(board, axis_second, d)
            if next_x and next_y:
                next_x = tuple(next_x)
                next_y = tuple(next_y)
                dist_dict[(next_x, next_y)] = min(dist_dict.get((next_x, next_y)), dist+1)
                robot.append((next_x, next_y))

        for 










solution([0, 1,2,3,4])

