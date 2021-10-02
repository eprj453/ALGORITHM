from pprint import pprint

availiable_traces = [
    [(1, 0), (0, 1), (0, 1)],
    [(1, 0), (1, 0), (0, -1)],
    [(1, 0), (1, 0), (0, 1)],
    [(1, 0), (0, -1), (0, -1)],
    [(1, 0), (0, -1), (0, 1)]
]


def can_remove(shape, block_number, board):
    n = len(board)
    floors = []

    bottom, top = 0, 50
    for s in shape:
        x, y = s
        bottom = max(bottom, x)
        top = min(top, x)

    print('bottom : ',bottom)
    direction = (-1, 0)
    for s in shape:
        # print(s)
        x, y = s
        dx, dy = direction
        # print(x+dx, y+dy)
        if x == bottom and 0 <= x+dx < n and 0 <= y+dy < n and board[x+dx][y+dy] != block_number:
            floors.append((x, y))

    print(floors)
    for f in floors:
        x, y = f
        dx, dy = direction
        while 0 <= x+dx < n and 0 <= y+dy < n:
            # print(x, y)
            if board[x+dx][y+dy]:
                return False
            x += dx
            y += dy

    return True


def get_trace(start: tuple, block_number: int, board: list):
    n = len(board)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    shape = [start]
    trace = []

    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True

    q = [start]

    while q:
        # print(q)
        x, y = q.pop(0)
        for direction in directions:
            dx, dy = direction
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if board[x+dx][y+dy] == block_number and not visited[x+dx][y+dy]:
                    visited[x + dx][y + dy] = True
                    q.append((x+dx, y+dy))
                    shape.append((x+dx, y+dy))
                    trace.append((dx, dy))

    return shape, trace


def remove_block(start, block_number, board):
    n = len(board)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    shape = [start]
    trace = []

    board[start[0]][start[1]] = 0

    q = [start]

    while q:
        x, y = q.pop(0)
        for direction in directions:
            dx, dy = direction
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if board[x+dx][y+dy] == block_number:
                    board[x+dx][y+dy] = 0
                    q.append((x+dx, y+dy))


    return board


def solution(board):
    answer = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                block_number = board[i][j]
                shape, trace = get_trace((i, j), block_number, board)
                if trace in availiable_traces:
                    is_can_remove = can_remove(shape, block_number, board)
                    if is_can_remove:
                        print('block number : ', block_number)
                        board = remove_block((i, j), block_number, board)
                        answer += 1

    pprint(board)

    print('answer : ', answer)
    return answer



solution([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,0,0,0],
    [0,0,0,0,0,0,4,4,0,0],
    [0,0,0,0,3,0,4,0,0,0],
    [0,0,0,2,3,0,0,0,0,5],
    [1,2,2,2,3,3,6,0,0,5],
    [1,1,1,0,6,6,6,0,5,5]])

# solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])