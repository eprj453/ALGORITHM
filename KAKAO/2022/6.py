from pprint import pprint
import numpy as np


def solution(board, skill):
    board = np.array(board)
    for s in skill:
        ty, r1, c1, r2, c2, degree = s # 0, 0, 3, 4
        # print(r1, c1, r2, c2)
        # print(f'{r1}:{r2} / {c1}:{c2}')
        if ty == 1:

            board[r1:r2+1, c1:c2+1] -= degree
        elif ty == 2:
            board[r1:r2+1, c1:c2+1] += degree

    cnt = np.count_nonzero(board > 0)
    print(cnt)
    # pprint(board > 0)
    # print(board)
    # answer = 0
    #
    # n, m = len(board), len(board[0])
    # memo = [0] * (n*m)
    #
    # for s in skill:
    #     ty, r1, c1, r2, c2, degree = s # 0, 0, 3, 4
    #     for idx in range(r1, r2+1):
    #         memo_idx_start, memo_idx_end = (idx*m) + c1, (idx*m) + c2
    #         if ty == 1:
    #             memo[memo_idx_start] -= degree
    #             memo[memo_idx_end] += degree
    #         else:
    #             memo[memo_idx_start] += degree
    #             memo[memo_idx_end] -= degree
    #
    #     pprint(memo)
    #
    # arr = []
    # cnt = 0
    # for i in range(0, n*m):
    #
    #     if memo[i] < 0:
    #         cnt += memo[i]
    #         i, j = i // m, i % m
    #         board[i][j] += cnt
    #         # cnt += memo[i]
    #     else:
    #
    #         i, j = i // m, i % m
    #         board[i][j] += cnt
    #         cnt += memo[i]
    #
    #
    # pprint(board)
    #
    #
    # return answer


solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
# solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])