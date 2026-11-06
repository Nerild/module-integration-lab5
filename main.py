
from input_module import input_matrix
from processing import find_valid_columns
from output import print_result


def main():
    print("Лабораторная работа № 5")
    print("Вариант 1")
    print("Поиск столбцов с элементами, кратными 5 или 7")
    print("-" * 50)

    for matrix_number in range(1, 3):
        print(f"\nМатрица № {matrix_number}")

        matrix = input_matrix()
        columns = find_valid_columns(matrix)
        print_result(matrix_number, columns)

    print("\nОбработка двух матриц завершена.")


if __name__ == "__main__":
    main()
