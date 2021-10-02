def get_alphabet(num: str):
    if num.startswith('0'):
        return 0
    return 1 if 1 <= int(num) <= 26 else 0


def get_alphabet_count(target_idx, letter):
    if 0 <= target_idx < n and letter:
        return alphabet_counts[target_idx]
    return 0


numbers = list(input())
n = len(numbers)
alphabet_counts = [0 for _ in range(n)]
alphabet_counts[0] = get_alphabet((numbers[0]))


def solution():
    for i in range(1, n):
        before_two, before_one = i-2, i-1
        one_letter, two_letter = get_alphabet(numbers[i]), get_alphabet(numbers[i-1] + numbers[i])
        alphabet_count = 0

        if i == 1 and two_letter:
            alphabet_count += 1

        one_letter_count, two_letter_count = \
            get_alphabet_count(before_one, one_letter), get_alphabet_count(before_two, two_letter)

        alphabet_count += (one_letter_count + two_letter_count)

        alphabet_counts[i] = alphabet_count

    answer = alphabet_counts[-1]
    print(alphabet_counts)
    print(answer % 1000000)
    print(alphabet_counts)

solution()
# print(get_alphabet(21))
# for i in range(1, 27):
#     print(chr(i+96))