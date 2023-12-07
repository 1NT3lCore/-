try:
    N = int(input("Введите количество строк и столбцов"))
except:
    print("Неверный тип данных")
    exit()
A = []
for i in range(N):
    row = []
    for j in range(N):
        try:
            value = int(input("Введите элемент [{}, {}]: ".format(i, j)))
        except:
            print("Неверный тип данных")
            exit()
        row.append(value)
    A.append(row)
for row in A:
    print(row)
for i in range(N):
    save = A[i][i]
    A[i][i] = A[i][N-1-i]
    A[i][N-1-i] = save
print("Результирующий список А:")
for row in A:
    print(row)

