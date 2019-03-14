import time

try:
    f = open('/Users/Andrefourme/PycharmProjects/byte/files/poem.txt')
    while True: # наш обычный способ читать файлы
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2) # пусть подождет некоторое время
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла')
finally:
    f.close()
    print('Очистка, закрытие файла')
