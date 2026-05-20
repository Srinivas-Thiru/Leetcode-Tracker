from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for counter, i in enumerate(nums):
            rem = target - i
            if rem in d:
                return [counter, d[rem]]
            d[i] = counter
        return []
