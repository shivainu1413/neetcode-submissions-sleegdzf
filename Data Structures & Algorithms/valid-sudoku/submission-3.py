class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_len = len(board)
        col_len = len(board[0])
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]
        for r in range(row_len):
            for c in range(col_len):
                val = board[r][c]
                if val == '.': continue
                box_index = (r//3) * 3 + c//3
                if val in row_sets[r] or val in col_sets[c] or val in box_sets[box_index]:
                    return False
                row_sets[r].add(val)
                col_sets[c].add(val)
                box_sets[box_index].add(val)
        return True
