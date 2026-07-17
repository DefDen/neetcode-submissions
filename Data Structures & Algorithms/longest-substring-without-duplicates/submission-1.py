class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        r = 0
        l = 0
        for c in s:
            while c in d:
                d.pop(s[l])
                l += 1
            d[c] = 1
            r = max(r, len(d))
        return r