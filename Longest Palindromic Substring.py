class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        ans = ""
        for i in range(len(s)):
            j = i + 1
            while j<=len(s) and len(ans) <= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(ans):
                    ans = s[i:j]
                j += 1
        return ans