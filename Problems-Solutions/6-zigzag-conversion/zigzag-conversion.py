class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        grid = [[] for _ in range(numRows)]
        curr = 0
        direction = 'd'
        for i in s:
            print(curr, direction)
            if curr == 0:
                direction = 'd'
            if curr == numRows-1:
                direction = 'u'
            if direction == 'u':
                grid[curr].append(i)
                curr -= 1
            if direction == 'd':
                grid[curr].append(i)
                curr += 1
        ans = ""
        for i in grid:
            ans += ''.join(i)
        return ans
