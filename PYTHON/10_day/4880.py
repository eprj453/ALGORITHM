import sys
sys.stdin = open('4880_input.txt', 'r')

def game(cards):
    if len(cards) == 1:
        return cards[0]

    left = game(cards[:(len(cards)+1)//2])
    right = game(cards[(len(cards)+1)//2:])

    if left[0] == right[0]:
        return left
    else:
        if left[0] == 1 and right[0] == 2:
            return right
        elif left[0] == 1 and right[0] == 3:
            return left
        elif left[0] == 2 and right[0] == 1:
            return left
        elif left[0] == 2 and right[0] == 3:
            return right
        elif left[0] == 3 and right[0] == 1:
            return right
        elif left[0] == 3 and right[0] == 2:
            return left

    return cards


for i in range(1, int(input())+1):
    n = int(input())
    in_cards = list(map(int, input().split()))
    card = []
    for j in range(n):
        temp = []
        temp.append(in_cards[j])
        temp.append(j+1)
        card.append(temp)
    ans = game(card)
    print(ans)
    print('#{} {}'.format(i, ans[1]))