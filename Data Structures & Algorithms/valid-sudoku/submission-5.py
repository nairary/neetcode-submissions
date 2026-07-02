class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = [set() for i in range(9)]
        row_set = [set() for i in range(9)]
        for j in range(0, 9, 3):
            for i in range(0, 9, 3):
                local_set = set()
                i_, j_ = i, j
                for _ in range(0, 3):
                    for _ in range(0, 3):
                        if board[i_][j_] != ".":
                            cur = int(board[i_][j_])
                            if cur in local_set:
                                return False
                            else:
                                local_set.add(cur)
                            
                            if cur in col_set[j_]:
                                return False
                            else:
                                col_set[j_].add(cur)

                            if cur in row_set[i_]:
                                return False
                            else:
                                row_set[i_].add(cur)
                        i_ += 1
                    j_ += 1
                    i_ = i
            print(f"col_set: {col_set}")
            print(f"row_set: {row_set}")
        return True

