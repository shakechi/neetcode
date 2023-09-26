class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        while start < len(nums):
            for i in range(start+1, len(nums)):
                if nums[start]+nums[i] == target:
                    return [start,i]
            start+=1