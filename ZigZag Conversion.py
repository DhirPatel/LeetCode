class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        lst = []
        for i in range(numRows):
            lst.append(i)
        for i in range(numRows-2,0,-1):
            lst.append(i)
        lst = lst * l
        ans = ""
        for i in range(numRows):
            for j in range(l):
                if lst[j] == i:
                    ans += s[j]
        return ans