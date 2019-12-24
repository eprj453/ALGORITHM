def comb(start, end, temp, visited, nums):
    global can_make
    if start == 4:
        front_time = int(temp[0]+temp[1])
        back_time = int(temp[2]+temp[3])
        if 0 <= front_time <= 23 and 0 <= back_time <= 59:
            can_make.add(''.join(temp))
        return
    else:
        for i in range(0, 4):
            if visited[i]: continue
            else:
                temp.append(str(nums[i]))
                visited[i] = True
                comb(start+1, end, temp, visited, nums)
                visited[i] = False
                temp.pop()



def solution(A, B, C, D):
    nums = [A, B, C, D]
    temp = []
    visited = [False] * 4
    comb(0, 4, temp, visited, nums)
    return len(can_make)

can_make = set()
print(solution(6,7,8,9))

