# Открываем файл для чтения
with open('F.txt', 'r') as file:
    content = file.readlines()

# Выводим содержимое файла до преобразования
print("Содержимое файла до преобразования:")
for line in content:
    print(line.strip())

# Преобразование элементов файла
for i in range(len(content)):
    number = int(content[i].strip())
    if number % 3 != 0:
        content[i] = str(number + (number % 3))

# Открываем файл для записи
with open('F.txt', 'w') as file:
    file.writelines(content)

# Выводим содержимое файла после преобразования
print("\nСодержимое файла после преобразования:")
for line in content:
    print(line.strip())