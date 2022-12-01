class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[]] #dp[0] = []
        dp.append(set(["()"])) #dp[1] = ["()"]
        
        for i in range(2, n+1):
            temp = set()
            for prefix in dp[i-1]:
                temp.add("(" + prefix + ")")

            for k in range(1, i):
                for sub1 in dp[i-k]:
                    for sub2 in dp[k]:
                        temp.add(sub1+sub2)
                
            dp.append(temp)
            
        return dp[-1]
            