try:
    M = int(input("Введите количество строк: "))
except:
    print("Неверный тип данных")
    exit()
try:
    N = int(input("Введите количество столбцов: "))
except:
    print("Неверный тип данных")
    exit()
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        try:
            value = int(input("Введите элемент [{}, {}]: ".format(i, j)))
        except:
            print("Неверный тип данных")
            exit()
        row.append(value)
    matrix.append(row)

print("\nИсходный список:")
for row in matrix:
    print(row)

min_value = matrix[0][0]
min_row = 0
min_column = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_row = i
            min_column = j
del matrix[min_row]
for row in matrix:
    del row[min_column]

print("\nПолученный список после удаления строки и столбца с минимальным элементом:")
for row in matrix:
    print(row)