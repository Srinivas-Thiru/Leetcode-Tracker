class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sumOflAndr = numbers[l] + numbers[r]
            if sumOflAndr == target: return [l+1,r+1] 
            if sumOflAndr > target: r -= 1
            if sumOflAndr < target: l += 1 

        return []

        