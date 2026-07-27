class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        h = set()
        ans = 0
        while r < len(s):
            while s[r] in h and l < r:
                h.remove(s[l])
                l += 1
            ans = max(ans, r-l+1)
            h.add(s[r])
            r += 1
        return ans


        
        