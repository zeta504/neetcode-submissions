class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        rows = [set() for _ in range(length)]
        columns = [set() for _ in range(length)]
        groups = [set() for _ in range(length)]

        for r in range(length):
            for c in range(length):
                val = board[r][c]
                if val != ".":
                    if val in rows[r]:
                        return False
                    rows[r].add(val)
                    if val in columns[c]:
                        return False
                    columns[c].add(val)
                    box_index = (r // 3) * 3 + (c // 3)
                    if val in groups[box_index]:
                        return False
                    groups[box_index].add(val)
        return True