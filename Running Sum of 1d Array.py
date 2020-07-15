class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runn = [0]
        for i in range(len(nums)):
            runn.append(runn[-1] + nums[i])
        return runn[1:]