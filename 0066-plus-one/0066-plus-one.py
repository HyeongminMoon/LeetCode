# 한자리씩 계산
# time: O(n)



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] != 9:
                digits[idx] += 1
                return digits
            # 올림
            digits[idx] = 0
        
        # 여기까지 왔다면, 맨 앞자리가 추가로 필요
        return [1] + digits