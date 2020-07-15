class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        digits = int(''.join(digits))
        digits = list(str(digits+1))
        return digits
        