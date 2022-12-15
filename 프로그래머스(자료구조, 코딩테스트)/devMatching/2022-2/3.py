memo = [0] * 51
memo[2] = 1
memo[3] = 1
memo[4] = 1
memo[5] = 5
memo[6] = 7
memo[7] = 0


def recursive(number, level):
    global memo
    if level == 0 and number == 6:
        return 6
    
    if number in [0, 1]:
        return 0

    elif memo[number] > 0:
        return memo[number]

    ans = 0
    for i in range(1, number):
        a, b = number-i, i
        print(a,b)
        res =  recursive(a, level+1) + recursive(b, level+1)
        print(res)
        ans += res
    
    return ans

print(recursive(7, 0))

