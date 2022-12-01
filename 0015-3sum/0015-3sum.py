class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        reverse_nums = [-n for n in nums]
        
        searched = set()
        for i, target in enumerate(reverse_nums):
            
            seen = {}
            for j, num in enumerate(nums):
                if i>=j: continue
                
                remain = target - num
                if num in seen:
                    searched.add(tuple(sorted([-target, remain, num])))
                else:
                    seen[remain] = num
        
            
        return searched