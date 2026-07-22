class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = (l + r) // 2
            print(nums[m])
            res = min(res, nums[m])
            if nums[m] < nums[l]:
                r = m - 1
            else:
                if nums[m] < nums[r] and nums[l] < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return res