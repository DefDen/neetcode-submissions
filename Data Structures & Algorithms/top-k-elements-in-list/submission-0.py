class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 0
            frequency_map[num] += 1
        tuples = []
        for key, freq in frequency_map.items():
            tuples.append((freq, key))
        print(tuples)
        return [key for freq, key in sorted(tuples)][-k:]