class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        l = len(nums)
        while i < l:
            temp = 0
            while i < l and nums[i] == 1:
                temp += 1
                i += 1
            ans = max(temp,ans)
            i += 1
        return ans