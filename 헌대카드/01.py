def selectMenberShip(price):
    if 0 <= price < 10000:
        return 0
    elif 10000 <= price < 20000:
        return 1
    elif 20000 <= price < 50000:
        return 2
    elif 50000 <= price < 100000:
        return 3
    else:
        return 4




def solution(purchase):
    answer = [0] * 5
    calender = [
        [0] * 31,
        [0] * 28,
        [0] * 31,
        [0] * 30,
        [0] * 31,
        [0] * 30,
        [0] * 31,
        [0] * 31,
        [0] * 30,
        [0] * 31,
        [0] * 30,
        [0] * 31
     ]
    print(calender)
    for p in purchase:
        date, price = p.split(' ')
        year, month, day = date.split('/')
        print('ymd : ' , year, month, day)
        i, j, k = 0, int(month)-1, int(day)-1
        while i < 30:
            print(i, j, k)
            # print(len(calender[j]))
            if j >= 12 : break
            # if j == 11 and k == 31: break
            if k == len(calender[j])-1:
                calender[j][k] += int(price)
                j += 1
                k = 0
            else:
                calender[j][k] += int(price)
                k += 1
            i += 1
    for i in range(12):
        for j in range(len(calender[i])):
            lv = selectMenberShip(calender[i][j])
            answer[lv] += 1
    return answer

# print(solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]))
print(solution(["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000", '2019/12/30 100000']))
