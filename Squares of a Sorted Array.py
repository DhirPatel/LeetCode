class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A1 = [i**2 for i in A]
        A1.sort()
        return A1