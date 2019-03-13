# 'ab' - сокращение от 'a'ddress'b'ook

ab = {'Swaroop' : 'swaroop@swaroopch.com',
      'Larry' : 'larry@wall.org',
      'Matsumoto' : 'matz@ruby-lang.org',
      'Spammer' : 'spammer@hotmail.com'
     }

print("Адрес Swaroop'a:", ab['Swaroop'])

# Удаление пары ключ-значение

del ab['Spammer']

print('n\В адресной книге {0} контактов\n', format(len(ab)))

for name, adress in ab.items():
    print('Контакт {0} с адресом {1}' .format(name, adress))

# Добавление пары ключ-значение

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])