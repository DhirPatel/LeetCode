class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l = len(arr)
        i = 0
        while i < l:
            try:
                temp = arr[:i] + arr[i+1:]
                temp = temp.index(arr[i] * 2)
                return True
            except:
                i += 1
        return False