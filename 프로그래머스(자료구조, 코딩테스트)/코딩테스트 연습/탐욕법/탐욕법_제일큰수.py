def solution(number, k):
    answer = ''
    nums = []
    for idx, num in enumerate(number):
        target = number[idx]
        while nums and nums[-1] < target:
            nums.pop()
            k -= 1
            if k == 0: break
        if k == 0:
            nums += number[idx:]
            break
        nums.append(num)

    nums = nums[:-k] if k > 0 else nums
    answer = ''.join(nums)
    return answer

# print(solution('4177252841', 4))
print(solution('1231234', 3))