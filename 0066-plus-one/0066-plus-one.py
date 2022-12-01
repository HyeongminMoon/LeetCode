class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(s) for s in str(int(''.join([str(d) for d in digits]))+1)]