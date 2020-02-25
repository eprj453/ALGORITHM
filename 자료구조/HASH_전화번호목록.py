def solution(phone_book):
    answer = True
    phone_numbers = {}
    for number in phone_book:
        if not answer:
            break
        else:
            for l in range(0, len(number)+1):
                print(number[0:l])
                res = phone_numbers.get(number[0:l])
                # print(res)
                if res != None and res > 0:
                    answer = False
                    break
            phone_numbers[number] = 1
        # print()
    return answer
print(solution(["119", "97674223", "1195524421"]))
# print(solution(['123','456','789']))