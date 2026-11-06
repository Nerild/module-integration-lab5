
def print_result(matrix_number, columns):
    """
    Выводит номера столбцов, содержащих
    только элементы, кратные 5 или 7.
    """

    print(f"\nРезультат для матрицы № {matrix_number}")
    print("-" * 40)

    if columns:
        print("Подходящие столбцы:")

        for column in columns:
            print(f"Столбец № {column}")

        print(f"Всего найдено: {len(columns)}")

    else:
        print("Столбцов, содержащих только элементы,")
        print("кратные 5 или 7, не найдено.")

    print("-" * 40)
