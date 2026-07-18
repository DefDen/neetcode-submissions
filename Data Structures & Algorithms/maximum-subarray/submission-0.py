class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m, curr = -10000, 0
        for n in nums:
            curr += n
            m = max(m, curr)
            curr = max(curr, 0)
        return m