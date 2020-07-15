class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        lst = [1,2]
        for i in range(3,n+1):
            lst.append(lst[-1] + lst[-2])
        return lst[-1]