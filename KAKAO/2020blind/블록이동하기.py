

def horizental_check(present, board):
    n = len(board)
    x1, y1, x2, y2 = present[0][0], present[0][1], present[1][0], present[1][1]
    result = []
    if 0 <= x1-1 < n and 0 <= y1 < n and 0 <= x2-1 < n and 0 <= y2 < n:
        if not board[x1-1][y1] and not board[x2-1][y2]:
            result.append(
                ((x1-1, y1), (x2-1, y2))
            )
            result.append(
                ((x2-1, y2-1), (x1, y1))
            )
            result.append(
                ((x1-1, y1+1), (x2, y2))
            )




    return result

def vertical_check():
    return []



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

    key = tuple(sorted([(0, 0), (0, 1)]))
    dist_dict[key] = 0
    robot = [((0, 0), (0, 1))]

    while robot:
        direction = robot.pop(0)

        x1, y1, x2, y2 = direction[0][0], direction[0][1], direction[1][0], direction[1][1]
        if x1 == x2:
            horizental_check([x1, y1], [x2, y2], n)












solution([0, 1,2,3,4])

