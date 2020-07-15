class Solution:
    def mySqrt(self, x: int) -> int:
        x = str(x ** 0.5)
        x = x.split(".")
        x = int(x[0])
        return x