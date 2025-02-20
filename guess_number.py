# Импорт функции получения случайных чисел
# из модуля random.
from random import randint
V = 125
# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print('Угадайте число от 1 до 100')

def main():
    while True:
        # Получаем число от пользователя и сохраняем его в переменную.
        guess_1 = int(input('Введите число: '))
        
        # Если число меньше загаданного...
        if guess_1 < number:
            # ...выводим сообщение.
            print('Ваше число меньше того, что загадано.')
        
        # Если число больше загаданного...
        elif guess_1 > number:
            # ...выводим сообщение.
            print('Ваше число больше того, что загадано.')
        
        # Если число угадано...
        elif guess_1 == number:
            # ...прерываем выполнение программы и...
            break

main()
# ...выводим сообщение.

print('Отличная интуиция! Вы угадали число :)')
