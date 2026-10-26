class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        best, water, base, height = 0, 0, 0, 0
        while j > i:
            first = heights[i]
            second = heights[j]
            height = min(first, second)
            water = height * (j - i)
            if water > best:
                best = water
            if first > second: j -= 1
            else: i += 1
        return best
            
