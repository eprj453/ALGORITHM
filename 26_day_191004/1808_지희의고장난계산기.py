import sys, time
sys.stdin = open('1808_input.txt', 'r')

start = time.time()

for i in range(1, int(input())+1):
    ope_count = 0
    nums = list(map(int, input().split()))
    set_num = int(input())
    aliquots = [set_num]
    c = set_num // 2
    while c >= 2:
        if set_num % c == 0:
            aliquots.append(c)
        c -= 1
    k = 0
    while set_num > 0:
        result1 = False
        for j in range(k, len(aliquots)):
            result2 = True
            aliquot = aliquots[j]
            for ali in str(aliquot):
                if nums[int(ali)] == 0:
                    result2 = False
                    break

            if result2 == True and set_num % aliquot == 0: # 가지고 있는 숫자로 만들 수 있는 약수 발견
                set_num /= aliquot
                ope_count += (len(str(aliquot))+1)
                # aliquots = aliquots[j:]
                k = j
                result1 = True
                break

        if set_num == 1:
            break

        if result1 == False: # 가지고 있는 약수 발견 못했을 시
            ope_count = 0
            break

    ope_count = -1 if ope_count == 0 else ope_count

    print('#{} {}'.format(i, (ope_count)))


print('time : {}'.format(time.time() - start))


    # # print(nums)
    # while set_num >= 1:
    #     # print(set_num)
    #     result = True
    #     for num in str(set_num):
    #         if int(num) not in nums:
    #             result = False
    #             break
    #     # print('first result : ', result)
    #     # print(set_num)
    #
    #     if result == True:
    #         ope_count += (len(str(set_num))+1)
    #         break
    #     else:
    #         result2 = False
    #         for num in nums:
    #             if num != 0 and num != 1 and set_num % num == 0:
    #                 set_num //= num
    #                 ope_count += 1
    #                 result2 = True
    #                 # result2 = True
    #                 break
    #         # print('second result : ', result2)
    #         if result2 == False:
    #             ope_count = -1
    #             break
    #         # else:continue
    #         # print(set_num)

    # print('#{} {}'.format(i, ope_count))

'''
1
0 0 0 0 0 0 0 0 0 1
793881

'''

    # while set_num > 1:
    #     result = False
    #     for j in nums:
    #         if set_num % j == 0:
    #             ope_count += 2
    #             set_num /= j
    #             result = True
    #             break
    #     if result == False: break
    #
    #     result2 = False
    #     for j in str(set_num):
    #         if int(j) in nums:
    #             result2 = True
    #             continue
    #         else:
    #             result2 = False
    #             break
    #
    #     if result2 == True:
    #         ope_count += (len(set_num)+1)
    #         break



    # if result == False:
    #     print(-1)
    # else:
    #     print(ope_count)
    # # print(nums)
    # print(set_num)
    # print('time : {}'.format(time.time() - start))