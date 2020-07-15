class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        lengths = list(map(len,strs))
        index = lengths.index(min(lengths))
        prefix = strs[index]
        strs = strs[:index] + strs[index+1:]
        while len(prefix) > 0:
            flag = 0
            for temp in strs:
                if prefix not in temp[:len(prefix)]:
                    prefix = prefix[:-1]
                    break
                else:
                    flag += 1
            if flag == len(strs):
                return prefix
        else:
            return ""