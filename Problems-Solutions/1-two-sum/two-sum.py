class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(0, len(nums)):
            bal = target - nums[i]
            if bal in dic:
                return [i, dic[bal]]
            dic[nums[i]] = i
        
        return [0,0]