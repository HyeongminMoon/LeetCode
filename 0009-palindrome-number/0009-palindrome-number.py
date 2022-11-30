class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        while(len(string) > 1 and string[0] == string[-1]):
            string = string[1:-1]
        return len(string) <= 1
        