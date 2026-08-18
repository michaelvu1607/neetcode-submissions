class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        cur_a = 0
        max_a = 0

        while l < r:
            cur_a = min(heights[l], heights[r]) * (r - l)
            max_a = max(cur_a, max_a)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_a