shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

# операция индексирования
print('Элемент 0 -', shoplist[0])
print('Элемент 1 -', shoplist[1])
print('Элемент 2 -', shoplist[2])
print('Элемент 3 -', shoplist[3])
print('Элемент -1 -', shoplist[-1])
print('Элемент -2 -', shoplist[-2])
print('Символ 0 -', name[0])

# Вырезка из списка
print('Элементы с 1 по 3:', shoplist[1:3])
print('Элементы со 2 по последний:', shoplist[2:])
print('Элементы с 1 по -1:', shoplist[1:-1])
print('Элементы с начала до конца:', shoplist[:])

# Вырезка из строки
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы с начала до конца:', name[:])
