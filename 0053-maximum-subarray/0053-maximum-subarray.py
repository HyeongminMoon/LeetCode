class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # pivot_idx = 0
        current_sum = 0
        max_sum = max(nums)
        for idx, n in enumerate(nums):
            if current_sum + n <= 0:
                # pivot_idx = idx + 1
                current_sum = 0
            else:
                current_sum += n
                max_sum = max(max_sum, current_sum)
                
        return max_sum