def solution(S):
    nums = ''
    for s in S:
        if s.isdigit():
            nums += s
    number = list(nums)
    l = len(number)
    n = 3
    while n < len(number)-2:
        number.insert(n, '-')
        n += 4
    # for n in range(3, l, 4):
    #     print(n)
    #     number.insert(n, '-')
    #     print(number)
    if l % 3 != 0:
        number.insert(-2, '-')

    return ''.join(number)

print(solution('555372654----2232222223---22222222225622342'))
