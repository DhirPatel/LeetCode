class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            i = 0
            while i < len(nums) and nums[i] < target:
                i += 1
            return i