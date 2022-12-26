from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        p1, p2 = 0, 0
        merged_nums = []
        while p1 < len(nums1) or p2 < len(nums2):
            if p1 >= len(nums1):
                while p2 < len(nums2):
                    merged_nums.append(nums2[p2])
                    p2 += 1
                break
            elif p2 >= len(nums2):
                while p1 < len(nums1):
                    merged_nums.append(nums1[p1])
                    p1 += 1
                break
            else:
                v1, v2 = nums1[p1], nums2[p2]
                if v1 > v2:
                    merged_nums.append(v2)
                    p2 += 1
                else:
                    merged_nums.append(v1)
                    p1 += 1
            
        
        median_value = merged_nums[n//2] if n % 2 else (merged_nums[(n//2)-1] + merged_nums[(n//2)]) / 2
        print(median_value)
        return median_value


s = Solution()
s.findMedianSortedArrays(nums1=[1,3], nums2=[2])
s.findMedianSortedArrays(nums1=[1,3], nums2=[2, 7])
s.findMedianSortedArrays(nums1=[1,2], nums2=[3,4])

