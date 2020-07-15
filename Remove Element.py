class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums and val in nums:
            nums.remove(val)
        return len(nums)