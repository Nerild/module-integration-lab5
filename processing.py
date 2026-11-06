
def is_valid_column(column):
    """
    Проверяет, что каждый элемент столбца
    кратен 5 или 7.
    """
    for number in column:
        if number % 5 != 0 and number % 7 != 0:
            return False

    return True


def find_valid_columns(matrix):
    """
    Находит номера столбцов, в которых
    все элементы кратны 5 или 7.
    """
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    valid_columns = []

    for j in range(cols):
        column = []

        for i in range(rows):
            column.append(matrix[i][j])

        if is_valid_column(column):
            valid_columns.append(j + 1)

    return valid_columns
