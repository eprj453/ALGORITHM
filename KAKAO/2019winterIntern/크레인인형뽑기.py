def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        i = 0
        while i < len(board):
            doll1 = board[i][m-1]
            if doll1 != 0:
                if not basket:
                    basket.append(doll1)
                else:
                    doll2 = basket[-1]
                    if doll1 == doll2:
                        print(basket)
                        print(doll1, doll2)
                        basket.pop()
                        answer += 2
                    else:
                        basket.append(doll1)
                board[i][m-1] = 0
                break
            i += 1
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))