from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        index = -1
        min_num = 10 ** 10
        for i in range(len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
                index = i


print(Solution())
