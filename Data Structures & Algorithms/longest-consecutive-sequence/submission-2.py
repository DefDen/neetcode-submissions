class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set(nums)
        longest = 1
        for n in nums:
            if n - 1 in s:
                continue
            curr = 1
            t = n + 1
            while t in s:
                curr += 1
                longest = max(curr, longest)
                t += 1
        return longest