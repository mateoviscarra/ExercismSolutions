def annotate(minefield):
    def count_adjacent_mines(row, col, minefield):
        rows, cols = len(minefield), len(minefield[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        total = 0
        for dr, dc in directions:
            if 0 <= row + dr < rows and 0 <= col + dc < cols and minefield[row + dr][col + dc] == '*':
                total += 1
        return total

    if not minefield:
        return []
    
    width = len(minefield[0])
    if any(len(row) != width for row in minefield):
        raise ValueError("The board is invalid with current input.")

    annotated_field = []
    for i, row in enumerate(minefield):
        annotated_row = ''
        for j, cell in enumerate(row):
            if cell == ' ':
                adjacent_mines = count_adjacent_mines(i, j, minefield)
                if adjacent_mines > 0:
                    annotated_row += str(adjacent_mines) 
                else:
                    annotated_row += ' '
            elif cell == '*':
                annotated_row += '*'
            else:
                raise ValueError("The board is invalid with current input.")
        annotated_field.append(annotated_row)
            
    return annotated_field
    