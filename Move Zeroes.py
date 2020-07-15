class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        l = len(nums)
        while i in nums:
            count += 1
            nums.pop(nums.index(i))
        for j in range(count):
            nums.append(0)