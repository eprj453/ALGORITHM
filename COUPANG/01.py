def solution(goods, coupons):
    answer = 0
    goods.sort(reverse=True)
    coupons.sort(reverse=True)
    print(goods)
    print(coupons)
    c = 0
    # c_rate, c_amount = 1 - (coupons[c][0] / 100), coupons[c][1]
    coupon_out = False
    for good in goods:
        c_rate = 1 - (coupons[c][0] / 100)
        # print('c, c_Rate , c_amount :  {}, {} , {}'.format(c, c_rate,c_amount))
        price, amount = good[0], good[1]

        if c == len(coupons):
            print("c : ",c)
            if coupons[c-1][1] == 0:
                print('남는 물건 {}원 {}개 추가'.format(price, amount))
                answer += price * amount

                continue

        while amount > 0:
            print(amount)
            if c == len(coupons) and coupons[c-1][1] == 0:
                answer += (price * amount)
                break
            else:
                if amount < coupons[c][1]: # 물건양 < 쿠폰양
                    print('물건 : {} >= 쿠폰 : {}'.format(amount, coupons[c][1]))
                    print(price, "원 물건에 ", c_rate, " 할인 적용 ", amount,"개")
                    # print('answer : ', answer)
                    #         print((price * (1 - (c_rate / 100))) * amount)
                    answer += (price * (1 - (coupons[c][0] / 100))) * amount # 모든 물건에 쿠폰 적용
                    print('answer : ', answer)
                    coupons[c][1] -= amount # 쿠폰 갯수 감소
                    # print('c_amount : {}'.format(c_amount))
                    amount = 0 # 적용시킬 물건 양 0
                else: # 물건양 > 쿠폰양
                    print('물건 : {} >= 쿠폰 : {}'.format(amount, coupons[c][1]))
                    print(price, "원 물건에 ", c_rate, " 할인 적용 ", coupons[c][1],"개")
                    answer += (price * (1 - (coupons[c][0] / 100))) * coupons[c][1] # 현재 할인율 남아있는 쿠폰 모두 소진
                    print('answer : ', answer)
                    amount -= coupons[c][1]
                    coupons[c][1] = 0
                    c += 1


    return answer
print(solution([[25400, 2], [10000, 1], [31600, 1]], [[5, 3], [23, 2], [11, 2], [9, 5]]))
# print(solution([[3100, 2], [7700, 1], [3100, 2]],[[33, 4]]))