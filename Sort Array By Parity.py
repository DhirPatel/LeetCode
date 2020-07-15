class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        temp = []
        i = 0
        while True:
            try:
                if A[i] % 2 == 1:
                    temp.append(A[i])
                    A.pop(i)
                else:
                    i += 1
            except:
                break
        return A[:] + temp[:]