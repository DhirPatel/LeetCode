class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0
        str = str.lstrip()
        if len(str) == 0:
            return 0
        pre = ''
        if str[0] == '-' or str[0] == '+':
            pre = str[0]
            str = str[1:]
        suff = ""
        for i in str:
            if i >= '0' and i <= '9':
                suff += i
            else:
                break
        if suff == '':
            return 0
        ans = int(pre + suff)
        if ans >= (2**31):
            return (2**31)-1
        elif ans < ((2**31)*-1):
            return (-1)*(2**31)
        else:
            return ans