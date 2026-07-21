import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-n, i) for i, n in enumerate(nums[:k])]
        heapq.heapify(max_heap)
        result = []
        for i in range(k, len(nums) + 1):
            while max_heap[0][1] < i - k or max_heap[0][1] >= i:
                heapq.heappop(max_heap)
            result.append(-max_heap[0][0])
            if i != len(nums):
                heapq.heappush(max_heap, (-nums[i], i))
        return result
