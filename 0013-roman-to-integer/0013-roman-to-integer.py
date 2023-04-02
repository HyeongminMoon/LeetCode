# 두글자씩 조사
# 예외케이스에 해당되면, 적용
# IV IX XL XC CD CM
# 예외케이스들은, 순서가 뒤집혔다는 특징이 있음.

# 아니면, 일반적용


class Solution:
    def romanToInt(self, s: str) -> int:
        map_table = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
            ' ': 0
        }
        
        result = 0
        pair = list(zip(s, s[1:] + ' '))
        idx = 0
        while(idx < len(s)):
            a, b = pair[idx]
            if map_table[a] < map_table[b]: # 예외 케이스
                result += map_table[b] - map_table[a]
                idx += 2 # 두 칸 전진
            else:
                result += map_table[a]
                idx += 1 # 한 칸 전진
                
        return result
                