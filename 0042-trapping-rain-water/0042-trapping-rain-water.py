class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_idx = 0
        max_height = 0
        temp_area = 0
        total_area = 0
        for i in range(n):
            if height[i] >= max_height:
                max_idx = i
                max_height = height[i]
                total_area += temp_area
                temp_area = 0
            else:
                temp_area += max_height - height[i]
        
        peak_idx = max_idx
        # backtrace
        max_idx = n-1
        max_height = 0
        temp_area = 0
        for i in range(n-1, peak_idx-1, -1):
            if height[i] >= max_height:
                max_idx = i
                max_height = height[i]
                total_area += temp_area
                temp_area = 0
            else:
                temp_area += max_height - height[i]
                
        return total_area