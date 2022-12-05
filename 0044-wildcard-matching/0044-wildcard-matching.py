class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S = len(s)
        P = len(p)
        dp = [[False]*(P+1) for _ in range(S+1)]
        
        dp[0][0] = True
        
        for j in range(1, P+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
                
        for i in range(1, S+1):
            for j in range(1, P+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] or (dp[i-1][j-1] and s[i-1] == p[j-1])
                    
        return dp[-1][-1]
        