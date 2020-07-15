class Solution:
    def reverse(self, x: int) -> int:
        pre = ''
        st = str(x)
        if st[0] == '-':
            pre = st[0]
            st = st[1:]
        st = st[::-1]
        st = pre + st
        ans = int(st)
        if ans >= ((2**31)*-1) and ans < (2**31):
            return ans
        else:
            return 0