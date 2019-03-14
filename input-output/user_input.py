def reverce(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverce(text)

somthing = input('Введите текст:')
if (is_palindrome(somthing)):
    print('Да, это палиндром')
else:
    print('Нет, это не палидром')

