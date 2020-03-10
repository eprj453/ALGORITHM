import math
primeArr = []
visited_dict = {}
ans = 0
def getPrimeNumber(number):
    primeArr = [False] * (number+1)
    arr = [0] * (number+1)
    for i in range(2, number+1):
        arr[i] = i
    # print(arr)
    for i in range(2, number+1, 1):
        if arr[i] == 0:
            continue
        for j in range(i+i, number+1, i):
            arr[j] = 0
    for i in range(2, number+1):
        if arr[i] != 0:
            primeArr[arr[i]] = True
    return primeArr

def perm(start, num, temp, visited):
    global ans
    if temp:
        if temp[0] == '0': return
        isDuplicated = visited_dict.get(''.join(temp))
        if isDuplicated == None and primeArr[int(''.join(temp))] == True:
            # print(''.join(temp))
            ans += 1
        visited_dict[''.join(temp)] = True
        if start == len(num): return

    for n in range(0, len(num)):
        if visited[n]: continue
        else:
            visited[n] = True
            temp.append(num[n])
            perm(start+1, num, temp, visited)
            temp.pop()
            visited[n] = False


def solution(numbers):
    global primeArr
    global ans
    answer = 0
    numbers = list(numbers)
    numbers.sort(reverse=True)
    primeArr = getPrimeNumber(int(''.join(numbers)))
    perm(0, ''.join(numbers), [], [False] * len(numbers))
    answer = ans
    return answer

                # print(numbers[j], end="")
        # print()
print(solution('17'))
# print(solution('011'))