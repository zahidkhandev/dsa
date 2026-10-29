class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i, row in enumerate(board):
            clean_row = [x for x in row if x !="."]
            set_clean_row = set(clean_row)
            if (len(set_clean_row) != len(clean_row)):
                return False

        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        for r_start in range(0, 9, 3):
            for c_start in range(0, 9, 3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        val = board[r_start + r][c_start + c]
                        if val != ".":
                            if val in seen:
                                return False 
                            seen.add(val)
            
        return True