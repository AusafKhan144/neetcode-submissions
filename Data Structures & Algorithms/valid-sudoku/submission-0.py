class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen_row = defaultdict(set)
        seen_columns = defaultdict(set)
        seen_boxes = defaultdict(set)

        for row_num, row_value in enumerate(board):
            for column_num, cell in enumerate(row_value):
                if cell == '.':
                    continue
                
                box_num = (row_num // 3) * 3 + (column_num//3)
                if cell in seen_row[row_num] or cell in seen_columns[column_num] or cell in seen_boxes[box_num]:
                    return False

                seen_row[row_num].add(cell)
                seen_columns[column_num].add(cell)
                seen_boxes[box_num].add(cell)

        return True