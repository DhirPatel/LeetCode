class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = list(s)
        if len(list(set(lst))) == len(lst):
            return len(lst)
        visited = [-1]*256
        visited[ord(s[0])] = 0
        n = len(lst)
        cur = 1
        ans = 1
        prev = 0
        i = 0
        for i in range(1,n):
            prev = visited[ord(s[i])]
            if prev == -1 or (i-cur > prev):
                cur += 1
            else:
                ans = max(ans,cur)
                cur = i - prev
            visited[ord(s[i])] = i
        return max(ans,cur)