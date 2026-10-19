class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(0, len(nums)):
            dic[nums[i]] = i
        
        for i in range(0, len(nums)):
            bal = target - nums[i]
            if bal in dic and dic[bal] != i:
                return [i, dic[bal]]
        
        return [0,0]