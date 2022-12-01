class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        
        arr = []
        for d in digits:
            arr.append(len(mapping[d]))

        # 333
        
        result = [''] * self.multiply(arr)
        
        for i, d in enumerate(digits):
            num_repeat = self.multiply(arr[i+1:])
            idx = 0
            while(idx < len(result)):
                for k in range(arr[i]):
                    letter = mapping[d][k]
                    for _ in range(num_repeat):
                        result[idx] += letter
                        idx += 1
                

        
        
        return result if len(result) > 1 else []
    

    def multiply(self , l: list) -> int:
        m = 1
        for _l in l:
            m *= _l
        return m