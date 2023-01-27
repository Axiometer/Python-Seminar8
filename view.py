"""Модуль взаимодействия с пользователем"""

num_class = ''

def main_menu() -> str:
    """Выбор класса"""
    global num_class
    while True:
        try:
            class_num = input('\nВведите класс: ')
            if class_num.lower() not in ['7а', '7б']:
                print('Доступны класс 7А или класс 7Б')
            elif class_num.lower() in ['7а', '7б']:
                path = class_num.upper() + '.txt'
                num_class = class_num

                return path
        except ValueError:
            print('Некорректный ввод! Введите число 1 или 2.')


def show_journal(journal: dict):
    """Вывести успеваемость всех учеников"""
    print(f'\nУспеваемость учеников в {num_class.upper()} классе:\n')
    for key in journal.keys():
        print(f'{key}:')
        j = 0
        for i, item in journal[key].items():
            j += 1
            print(f'\t{j}. {i}: ', end=' ')
            print(*item)
        print()

def get_name() -> str:
    """
    Запрос имени ученика.
    :return: Фамилия и имя ученика с заглавных букв.
    """
    name = input('Введите фамилию и имя ученика через пробел: ')
    print()
    return name.title().strip()


def get_lesson() -> str:
    """Запрос названия дисциплины"""
    lesson = input('Введите название предмета: ')
    print()
    return lesson.capitalize().strip()


def show_message(text: str):
    """Вывод сообщения в консоль"""
    print(text)


def show_pupil_lessons(journal: dict, name: str):
    """Вывести успеваемость конкретного ученика по всем предметам"""
    print(f'Ученик {num_class.upper()} класса {name}')
    for key in journal.keys():
        print(f'\t{key}:', end=' ')
        for i, item in journal[key].items():
            if i == name:
                print(*item)


def show_pupil_lesson(journal: dict, name: str, lesson: str):
    """Вывести успеваемость конкретного ученика по заданному предмету"""
    print(f'Ученик {num_class.upper()} класса {name}')
    print(f'\t{lesson}: ', end=' ')
    print(*journal[lesson][name])


def menu_teacher():
    """Вывод меню для учителя"""
    menu_list = [
        'Список всех учеников',
        'Успеваемость всех учеников по всем дисциплинам',
        'Успеваемость учеников по предмету',
        'Контроль знаний ученика',
        'Выход',
    ]

    print('\n=========== Главное меню ===========')
    for i, item in enumerate(menu_list):
        print(f'\t{i + 1}. {item}')


def command_teacher() -> int:
    """Команды учителя"""
    while True:
        try:
            menu_teacher()
            command = int(input('\nВведите номер команды: '))
            if command < 1 or command > 5:
                print('Введите номер команды от 1 до 5!')
            else:
                return command
        except ValueError:
            print('Некорректный ввод! Введите число 1 или 5.')


def show_list_pupils(journal: dict):
    """Вывод списка учеников в консоль"""
    print(f'\nСписок всех учеников в {num_class.upper()} классе: ')
    for item in journal.values():
        i = 0
        for key in item.keys():
            i += 1
            print(f'\t{i}. {key}')
        break


def show_progress_lesson(journal: dict, lesson: str):
    """Успеваемость по предмету"""
    print(f'\nУспеваемость учеников {num_class.upper()} класса')
    print(f'Дисциплина: {lesson.lower()}\n')
    i = 0
    for key, value in journal[lesson].items():
        i += 1
        print(f'\t{i}. {key}: ', end=' ')
        print(*value)


def control() -> int:
    """
    Контроль знаний ученика.
    :return: оценка.
    """
    while True:
        try:
            mark = int(input('Введите полученную отметку: '))
            if mark not in [1, 2, 3, 4, 5]:
                print('Введите отметку от 1 до 5.')
            elif mark in [1, 2, 3, 4, 5]:
                return mark
        except ValueError:
            print('Некорректный ввод! Введите число 1 или 5.')
