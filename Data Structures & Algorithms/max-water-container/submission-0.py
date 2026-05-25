class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            max_area = max(area,max_area)
            
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1
                
        return max_area

