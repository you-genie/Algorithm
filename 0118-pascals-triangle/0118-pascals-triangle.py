class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for i in range(1, numRows):
            bf_row = [0] + ret[i-1]
            curr_row = bf_row.copy()
            for j in range(len(bf_row)-1):
                curr_row[j] = bf_row[j] + bf_row[j+1]
            ret.append(curr_row)
        return ret