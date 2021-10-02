def is_prime_number(number):
    for i in range(2, number):
        if not number % i:
            return 0
    return 1


def encode_num(number, n):
    if number < n:
        return str(number)
    s = encode_num(number//n, n)
    return s + str(number % n)


print(encode_num(11, 2))

def solution(n, k):
    answer = 0

    encoded_number = encode_num(n, k)
    splited_number = encoded_number.split('0')

    for number in splited_number:
        if number and int(number) >= 2:
            answer += is_prime_number(number)

    return answer


solution(437674, 3)
solution(110011, 10)