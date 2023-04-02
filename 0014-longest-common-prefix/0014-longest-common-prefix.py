# string0를 기준 잡고, 한 단어씩 검사.
# 이때의 longest prefix를 다시 기준으로. 반복
# time: O(n)
# space: O(1)



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pivot = strs[0]
        for string in strs[1:]:
            # pivot string 비교 -> new pivot
            new_pivot = ""
            for i in range(min(len(pivot), len(string))):
                if pivot[i] == string[i]:
                    new_pivot += pivot[i]
                else:
                    break
            
            pivot = new_pivot
            
        
        return pivot