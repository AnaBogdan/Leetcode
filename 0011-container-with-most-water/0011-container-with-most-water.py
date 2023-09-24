class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, area = 0, 0
        right = len(height) - 1
        while right > left:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -=1
        return area
