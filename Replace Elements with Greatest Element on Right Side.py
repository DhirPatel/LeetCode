class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        i = 0
        while i < l - 1:
            arr[i] = max(arr[i+1:])
            i += 1
        arr[-1] = -1
        return arr