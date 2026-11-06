
def input_matrix():
    while True:
        try:
            rows = int(input("Введите количество строк (1-10): "))
            cols = int(input("Введите количество столбцов (1-10): "))

            if 1 <= rows <= 10 and 1 <= cols <= 10:
                break

            print("Ошибка: размеры должны быть от 1 до 10.")

        except ValueError:
            print("Ошибка: введите целое число.")

    matrix = []

    for i in range(rows):
        row = []

        for j in range(cols):
            while True:
                try:
                    value = int(input(
                        f"Элемент [{i + 1}][{j + 1}]: "
                    ))

                    if value <= 0:
                        print("Введите натуральное число.")
                        continue

                    row.append(value)
                    break

                except ValueError:
                    print("Ошибка: введите целое число.")

        matrix.append(row)

    return matrix

