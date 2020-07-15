class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lst = [-1,-1]
        try:
            lst[0] = nums.index(target)
        except:
            return lst
        nums = nums[::-1]
        lst[1] = nums.index(target)
        lst[1] = len(nums) - lst[1] - 1
        return lst