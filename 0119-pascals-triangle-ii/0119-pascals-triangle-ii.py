class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        past_row, curr_row = [1], [1]
        
        for _ in range(1, rowIndex+1):
            curr_row = [past_row[i]+past_row[i+1] for i in range(len(past_row)-1)]
            curr_row = [1] + curr_row + [1]
            past_row = curr_row
        
        return curr_row