# hand에 하나 들고 있음
# 삽입 포인터도 들고 있음
# 새로운게 들어오면 삽입하고 삽입 포인터 한칸 이동
# 들어왔던게 들어오면 변경없음

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hand = nums[0]
        pointer = 1
        for num in nums[1:]:
            if num == hand: continue
            nums[pointer] = num
            pointer += 1
            hand = num
            
        return pointer
        