class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s)  for _ in range(len(s))]
        
        answer = ''
        for i in range(len(s)):
            dp[i][i] = True
            answer = s[i]
            
        maxLen = 1
        for start in range(len(s)-1, -1, -1):
            for end in range(start+1, len(s)):             
                if s[start] == s[end]:
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if len(answer) < end - start + 1:
                            answer = s[start: end+ 1]
        
        return answer