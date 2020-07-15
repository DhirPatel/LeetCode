class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for i in range(n):
            for l in self.generateParenthesis(i):
                for r in self.generateParenthesis(n-i-1):
                    ans.append('({}){}'.format(l,r))
        return ans