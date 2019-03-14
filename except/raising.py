class ShortInputException(Exception):
    '''Пользовательский класс исключений'''
    def __init__(self, lenght, atleast):
        Exception.__init__(self)
        self.lenght = lenght
        self.atleast = atleast

try:
    text = input('Введите что-нибудь -->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
        # Здесь может происходить обычная работа
except EOFError:
    print('Ну зачем ты мне сделал EOF?')
except ShortInputException as ex:
    print('ShortInputException: длина введеной строки -- {0}; \
            ожидалось, как минимум, {1}'.format(ex.lenght, ex.atleast))

else:
    print('Не было исключений')
