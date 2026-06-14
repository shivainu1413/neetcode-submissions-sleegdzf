class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_list = [set() for _ in range(9)]
        col_list = [set() for _ in range(9)]
        box_list = [set() for _ in range(9)]
        row_len = len(board)
        col_len = len(board[0])
        for r in range(row_len):
            for c in range(col_len):
                val = board[r][c]
                if val == '.':
                    continue
                box_index = (r//3) * 3 + (c//3)
                if val in row_list[r] or val in col_list[c] or val in box_list[box_index]:
                    return False
                row_list[r].add(val)
                col_list[c].add(val)
                box_list[box_index].add(val)
        return True