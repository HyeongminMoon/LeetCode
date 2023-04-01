class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        rows = [[1]]
        for _ in range(numRows - 1):
            row = self.next_row(row)
            rows.append(row)
            
        return rows
        
    def next_row(self, row):
        next_row = []
        for a, b in zip([0] + row, row + [0]):
            next_row.append(a + b)
        return next_row