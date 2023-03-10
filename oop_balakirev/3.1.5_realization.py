class LessonItem:
    __attrs = {'title': str, 'practice': int, 'duration': int}
    __positive = ['practice', 'duration']
    __not_del = ['title', 'practice', 'duration']

    def __init__(self, title, practice, duration):
        self.title = title
        self.practice = practice
        self.duration = duration

    @classmethod
    def __check_input(cls, key, value):
        if key in cls.__attrs:  # Если есть такой аттрибут.
            correct_type = cls.__attrs[key]
            if isinstance(value, correct_type):  # Если тип соответсвует.
                if key in cls.__positive:  # Если число должно быть полож.
                    if value < 0:
                        raise ValueError(f'Введите полож. значение {key}.')
                    return isinstance(value, correct_type)
                return isinstance(value, correct_type)
            raise TypeError(f'Неверный тип присваиваемых данных для {key}.')
        raise AttributeError(f'Аттрибута {key} не существует.')

    def __setattr__(self, key, value):
        if self.__check_input(key, value):
            object.__setattr__(self, key, value)

    def __getattribute__(self, key):
        return object.__getattribute__(self, key)

    def __getattr__(self, key):
        return False

    def __delattr__(self, key):
        if key in self.__attrs:
            if key in self.__not_del:
                raise AttributeError(f'Аттрибут {key} нельзя удалять.')
            object.__delattr__(self, key)
        raise AttributeError(f'Аттрибута {key} не существует.')


class Module:
    __attrs = {'name': str, 'lessons': list, 'lesson': LessonItem}

    def __init__(self, name):
        self.name = name
        self.lessons = list()

    @classmethod
    def __check_input(cls, key, value):
        if key in cls.__attrs:
            correct_type = cls.__attrs[key]
            if isinstance(value, correct_type):
                return isinstance(value, correct_type)
            raise TypeError(f'Неверный тип присваиваемых данных для {key}.')
        raise AttributeError(f'Аттрибута {key} не существует.')

    def add_lesson(self, lesson):
        """Добавление в конец списка lessons нового объекта LessonItem."""
        self.lesson = lesson
        self.lessons.append(self.lesson)
        del self.lesson

    def remove_lesson(self, indx):
        """Удаление из списка lessons урока по индексу indx."""
        if len(self.lessons) <= indx:
            raise IndexError('Веденный индекс больше чем элементов в списке.')
        self.lessons.pop(indx)

    def __setattr__(self, key, value):
        if self.__check_input(key, value):
            object.__setattr__(self, key, value)


class Course:
    __attrs = {'name': str, 'modules': list, 'module': Module}

    def __init__(self, name):
        self.name = name
        self.modules = list()

    @classmethod
    def __check_input(cls, key, value):
        if key in cls.__attrs:
            correct_type = cls.__attrs[key]
            if isinstance(value, correct_type):
                return isinstance(value, correct_type)
            raise TypeError(f'Неверный тип присваиваемых данных для {key}.')
        raise AttributeError(f'Аттрибута {key} не существует.')

    def add_module(self, module):
        """Добавление в конец списка modules нового объекта Module."""
        self.module = module
        self.modules.append(self.module)
        del self.module

    def remove_module(self, indx):
        """Удаление из списка modules модуля по индексу indx."""
        if len(self.modules) <= indx:
            raise IndexError('Веденный индекс больше чем элементов в списке.')
        self.modules.pop(indx)

    def __setattr__(self, key, value):
        if self.__check_input(key, value):
            object.__setattr__(self, key, value)
