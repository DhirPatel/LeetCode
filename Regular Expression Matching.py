class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*":
            return True
        if len(s) == 0:
            if len(p) == 0:
                return True
        if len(p) == 0:
            return False
        if ('.' not in p) and ('*' not in p):
            return s == p
        ans = re.search(p,s)
        try:
            ans = ans.group()
            return ans == s
        except:
            return False