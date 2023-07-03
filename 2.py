# Ввод двух одномерных массивов A1 и A2
A1 = input("Введите элементы массива A1 через пробел: ").split()
A2 = input("Введите элементы массива A2 через пробел: ").split()

# Вывод массивов A1 и A2
print("Массив A1:", A1)
print("Массив A2:", A2)

# Находим минимальное значение в A1
min_value = min(A1)

# Формируем массивы f1 и f2 из элементов до минимального значения
f1 = A1[:A1.index(min_value)]
f2 = A2[:A2.index(min_value)]

# Записываем массивы f1 и f2 в файлы
with open('f1.txt', 'w') as file:
    file.write('\n'.join(f1))

with open('f2.txt', 'w') as file:
    file.write('\n'.join(f2))

# Вывод массивов f1 и f2
print("Массив f1:", f1)
print("Массив f2:", f2)