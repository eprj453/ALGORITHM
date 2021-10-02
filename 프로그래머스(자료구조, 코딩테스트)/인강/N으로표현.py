

'''
N	number	return
5	12	4
2	11	3
'''


def solution(N, number):
    minimal_count = -1
    numbers = [set() for i in range(9)]

    # numbers[1].add(N) # 숫자를 1번 사용해서 만들 수 있는 숫자는 N 하나 뿐

    for i in range(1, 9):
        numbers[i].add(int(str(N)*i))

    # for i, x in enumerate(numbers, start=1):
    #     x.add(int(str(N) * i))

    # print(numbers)

    for i in range(1, 9):
        # 숫자를 i번 사용해서 만들 수 있는 경우의 수 따져보기
        for j in range(i):
            for op1 in numbers[j]:
                for op2 in numbers[i-j]:
                    numbers[i].add(op1 + op2)
                    numbers[i].add(op1 - op2)
                    numbers[i].add(op1 * op2)
                    if op2:
                        numbers[i].add(op1 // op2)
            # print(i, j)
        if number in numbers[i]:
            minimal_count = i
            break

    return minimal_count


print(solution(5, 12))