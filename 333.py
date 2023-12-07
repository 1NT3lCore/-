try:
    n = int(input("Введите кол-во слов в словаре: "))
except:
    print("Неверный тип данных")
    exit()
dictionary = {}  # создаем пустой словарь

for i in range(n):
    try:
        word, definition = input("Введите слово и его определение через двоеточие и пробел: ").split(": ")
    except:
        print("Неверный тип данных")
        exit()
    dictionary[word] = definition
print(n)
for key, value in dictionary.items():
    print(f"{key}, {value}")
search = input("Введите слово для поиска определения: ")
if search in dictionary:
    print(f"Определение для слова {search}: {dictionary[search]}")
else:
    print(f"Определение для слова {search} не найдено.")

