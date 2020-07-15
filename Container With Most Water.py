class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = min(height[0],height[-1]) * (len(height)-1)
        i = 0
        j = len(height) - 1
        while i < j:
            ans = max(ans,min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans 