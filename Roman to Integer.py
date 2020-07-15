class Solution:
    def romanToInt(self, s: str) -> int:
        _hash = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        n = len(s) - 1
        for i in range(n):
            if(_hash[s[i+1]] > _hash[s[i]]):
                ans = ans - _hash[s[i]]
            else:
                ans = ans + _hash[s[i]]
        
        ans = ans + _hash[s[len(s)-1]]
        
        return ans