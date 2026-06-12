class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_list = [set() for _ in range(9)]
        row_list = [set() for _ in range(9)]
        box_list = [set() for _ in range(9)]
        row_len = len(board)
        col_len = len(board[0])
        for r in range(row_len):
            for c in range(col_len):
                box_index = r // 3 * 3 + c // 3 
                if board[r][c] == '.':
                    continue
                if board[r][c] in row_list[r] or board[r][c] in col_list[c] or board[r][c] in box_list[box_index]:
                    return False
                row_list[r].add(board[r][c])
                col_list[c].add(board[r][c])
                box_list[box_index].add(board[r][c])
        return True