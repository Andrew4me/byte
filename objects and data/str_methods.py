name = 'swaroop' # Это объект строки

if name.startswith('swa'):
    print('Да, строка начинается на "swa"')

if 'a' in name:
    print('Да она содержит строку "а"')

if name.find('war') != -1:
    print('Да, она содержит строку "war"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))