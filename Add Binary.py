class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        s = a+b
        s = str(bin(s))
        return s[2:]