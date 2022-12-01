class Solution:
    def reverse(self, x: int) -> int:
        sign, num = (True, x) if x >= 0 else (False, -x)
        max32 = 2**31 - 1
        
        s = 0
        while(num > 0):
            cur = num % 10
            if s + cur / 10. > max32 / 10.:
                return 0
            s = s*10 + cur
            num //= 10
            
        return s if sign else -s