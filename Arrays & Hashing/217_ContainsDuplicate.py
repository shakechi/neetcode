class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flg = False
        nums.sort()

        for i,value in enumerate(nums[:len(nums)-1]):
            if value == nums[i+1]: 
                flg=True
                break
        return flg