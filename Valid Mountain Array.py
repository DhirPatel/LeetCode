class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        l = len(A)
        if l < 3:
            return False
        A.append(A[-1] - 1)
        i = 0
        while i < l and A[i] < A[i+1]:
            i += 1
        if i == l - 1 or i == 0:
            return False
        while i < l and A[i] > A[i+1]:
            i += 1
        if i == l:
            return True
        return False