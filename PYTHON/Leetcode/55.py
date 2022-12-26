from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        start, end = 0, n-1
        for idx in range(start, n):
            num = nums[idx]
            if n-1 <= idx + num < n:
                return True
        return False


s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([0,1]))
print(s.canJump([0]))
print(s.canJump([1]))