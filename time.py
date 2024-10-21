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

