class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in memo:
                memo[sortedWord] = []
            memo[sortedWord].append(word)
        ans = []
        for key in memo:
            curr = []
            val = memo[key]
            for i in val:
                curr.append(i)
            ans.append(curr)
        return ans
                
