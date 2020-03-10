def solution(prices):
    answer = []
    stk = []
    # for idx, price in enumerate(prices):
    #     # stkPrice = [idx, price, 0]
    #     if stk:
    #         day = 0
    #         while stk[-1][1] > price:
    #             stkPop = stk.pop()
    #             answer[stkPop[0]] = 1 + day
    #             day += 1
    #         stk.append([idx, price, day])
    #     else:
    #         stk.append([idx, price, 0])
    #
    # days = 0
    # while stk:
    #     # print(stk)
    #     stkPop = stk.pop()
    #     if answer[stkPop[0]] == 0:
    #         answer[stkPop[0]] = days
    #     if stkPop[2] > 0:
    #         days += stkPop[2]
    #     days += 1

    stk = []
    days = 0
    for i in range(len(prices)-1, -1, -1):
        print(stk)
        if not stk:
            answer.append(days + len(stk))
            stk.append(prices[i])
        else:
            popDay = 0
            while stk and stk[-1] < prices[i]:
                stk.pop()
                popDay += 1
            # if popDay > 0:
            if popDay == 0:
                answer.append(len(stk)+days + popDay)
                # days += popDay
            else:
                answer.append(days + popDay)
                days += popDay
            stk.append(prices[i])


    return list(reversed(answer))


# 입력 : [ 1, 2, 3, 2, 3, 1 ]
# 출력 : [ 5, 4, 1, 2, 1, 0 ]
#
# 입력 : [ 3, 1 ]
# 출력 : [ 1, 0 ]
# print(solution([1, 2, 3, 2, 3]))
print(solution([1,2,3,2,3,1]))