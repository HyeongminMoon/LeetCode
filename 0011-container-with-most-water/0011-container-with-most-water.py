class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        
        max_area = 0
        while(left < right):
            max_area = max(max_area, self.calcArea(left, height[left], right, height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
        
    def calcArea(self, x1: int, y1: int, x2: int, y2: int) -> int:
        if x1==x2: return 0
        return abs(x2-x1)*min(y1, y2)
            
                    
        