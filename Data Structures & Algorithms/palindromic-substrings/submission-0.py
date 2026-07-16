class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 1
        for i in range(len(s) - 1):
            j = 0
            while i + j < len(s) and i - j >= 0 and s[i + j] == s[i - j]:
                total += 1
                j += 1
            if s[i] == s[i + 1]:
                j = 0
                while i + 1 + j < len(s) and i - j >= 0 and s[i + 1 + j] == s[i - j]:
                    total += 1
                    j += 1
        return total
