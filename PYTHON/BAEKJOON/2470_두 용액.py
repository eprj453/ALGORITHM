n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

# print(liquids)

start, end = 0, n-1

answer, answer_abs = [0, 0], 2_000_000_001

while start < end:
    print(liquids[start], liquids[end])
    s = liquids[start] + liquids[end]
    if abs(s) < abs(answer_abs):
        print('get!')
        answer = [liquids[start], liquids[end]]
        answer_abs = s

    if s == 0:
        start += 1
        end -= 1
    elif s > 0:
        end -= 1
    else:
        start += 1

print(f'{answer[0]} {answer[1]}')