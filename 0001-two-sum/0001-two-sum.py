class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_inds = sorted(range(len(nums)), key=lambda k: nums[k])
        sorted_nums = [nums[k] for k in sorted_inds]
        
        i, j = 0, len(nums) - 1
        while(i < j):
            number = sorted_nums[i] + sorted_nums[j]
            if number == target:
                return [sorted_inds[i], sorted_inds[j]]  
            elif number > target:
                j -= 1
            elif number < target:
                i += 1
                
        # no answer
            