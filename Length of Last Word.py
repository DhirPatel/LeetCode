class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.strip().split()
        if len(lst) == 0:
            return 0
        else:
            temp = lst[-1]
            if temp.strip() == "":
                return 0
            else:
                return len(temp.strip())