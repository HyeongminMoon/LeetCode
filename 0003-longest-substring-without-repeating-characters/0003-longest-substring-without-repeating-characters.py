class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_str = ""
        max_len = 0
        for _letter in s:
            cur_str = cur_str.split(_letter)[-1] + _letter
            if len(cur_str) > max_len:
                max_len = len(cur_str)
        return max_len
                