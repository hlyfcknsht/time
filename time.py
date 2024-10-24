"""

Напишите программу time.py, которая получает из первого аргумента командной строки количество секунд, которое прошло с начала дня. Программа должна выводить отформатированное время в формате HH:MM:SS.

SS – число секунд от 0 до 59.
MM – число минут от 0 до 59.
HH – число часов от 0 до 23.
Все значения времени должны выводится в двузначном формате, если число занимает один знак, то перед ним должен быть 0.

Если прошло меньше одного часа, то часы выводить не нужно.

Если прошло меньше одной минуты, то минуты выводить не нужно.

Пример использования:
> python time.py 17
17
> python time.py 79
01:19
> python time.py 4589
01:16:29

"""

import sys


def time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60

    # Форматируем строку в зависимости от значений часов, минут и секунд
    if hours > 0:
        return f'{hours:02}:{minutes:02}:{sec:02}'
    elif minutes > 0:
        return f'{minutes:02}:{sec:02}'
    else:
        return f'{sec:02}'


print(time(int(sys.argv[1])))

