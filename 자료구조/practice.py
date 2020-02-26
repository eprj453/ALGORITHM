import copy
def comb(arr, temp, visited, end, k):
    global num
    global ans
    print('ans : ', ans)
    if not ans:
        if len(temp) == end:
            if num == k:
                ans = temp.copy()
                print(ans)
            else:
                num += 1
            return

        for i in range(0, end):
            if visited[i]: continue
            else:
                visited[i] = True
                temp.append(arr[i])
                comb(arr, temp, visited, end, k)
                visited[i] = False
                temp.pop()

num = 1
ans = []
comb([1,2,3], [], [False] * 3, 3, 5)
print(ans)
# def solution(n, k):
#     answer = []
#     return answer