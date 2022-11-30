class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return s[::numRows * 2 - 2] + ''.join([l + s[numRows * 2 - i - 2::numRows * 2 - 2][k] if k < len(s[numRows * 2 - i - 2::numRows * 2 - 2]) else l for i in range(1, numRows-1) for k, l in enumerate(s[i::numRows * 2 - 2])]) + s[numRows - 1::numRows * 2 - 2] if numRows > 1 else s