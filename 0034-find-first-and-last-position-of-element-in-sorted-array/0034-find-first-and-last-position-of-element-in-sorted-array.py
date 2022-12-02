class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if len(nums) == 0: return result
        # find start
        left = 0
        right = len(nums) - 1
        while(left < right):
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] == target:
            result[0] = left
        else:
            return result
                
        # find end
        right = len(nums) - 1
        while(left < right):
            mid = (left + right) // 2 + 1
            
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        
        result[1] = right
        
        return result