class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        dp = [[(-1, C, 0)]*C for _ in range(R)]                                                 # default (left=-1, right=C, height=0) , dp[R][C]

        for col in matrix:                                                                      # append 0 to right side for a convenience
            col.append(0)

        left, right = -1, C
        searched = {}                                                                           # result dict
        for r, row in enumerate(matrix):            
            for c, num in enumerate(row):
                if num == '1':                                                                  # stack locations until '1' ends
                    left = c if left == -1 else left
                    right = c
                elif left != -1:                                                                # when reach '0', if there is location stack, upload it to dp table
                    if r == 0:                                                                  # iniciate at row 0
                        height = 1
                        for ci in range(left, right+1):
                            dp[r][ci] = (left, right, height)
                            if (left, right, height) not in searched:                           # update result dict
                                searched[(left, right, height)] = (right - left + 1) * height
                    else:
                        for ci in range(left, right+1):
                            _left = max(left, dp[r-1][ci][0])
                            _right = min(right, dp[r-1][ci][1])
                            _height = dp[r-1][ci][2] + 1
                            dp[r][ci] = (_left, _right, _height)
                            if (_left, _right, _height) not in searched:                        # update result dict
                                searched[(_left, _right, _height)] = (_right - _left + 1) * _height
                    left, right = -1, C                                                         # reset to default value after uploading location stack

        return max(searched.values()) if searched else 0
