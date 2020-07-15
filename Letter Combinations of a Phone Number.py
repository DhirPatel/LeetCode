class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        _hash = {'2' : ['a','b','c'],
                 '3' : ['d','e','f'],
                 '4' : ['g','h','i'],
                 '5' : ['j','k','l'],
                 '6' : ['m','n','o'],
                 '7' : ['p','q','r','s'],
                 '8' : ['t','u','v'],
                 '9' : ['w','x','y','z']}
        def sol(pattern,lst):
            if len(lst) == 0:
                ans.append(pattern)
            else:
                for item in _hash[lst[0]]:
                    sol(pattern + item , lst[1:])
        
        ans = []
        if len(digits) > 0:
            sol("",digits)
        return ans