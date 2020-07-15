class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        height = heights[:]
        height.sort()
        for i in range(len(height)):
            if height[i] != heights[i]:
                count += 1
        return count