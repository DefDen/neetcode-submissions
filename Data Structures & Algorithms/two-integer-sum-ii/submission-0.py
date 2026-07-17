class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = [0, len(numbers) - 1]
        while numbers[r[0]] + numbers[r[1]] != target:
            if numbers[r[0]] + numbers[r[1]] < target:
                r[0] += 1
            else:
                r[1] -= 1
        r[0] += 1
        r[1] += 1
        return r