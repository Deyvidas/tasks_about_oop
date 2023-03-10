class Picture:
    __attrs = {'name': str, 'author': str, 'descr': str}

    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr

    def __setattr__(self, key, value):
        if self.__check_input(key, value):
            object.__setattr__(self, key, value)

    def __getattribute__(self, key):
        return object.__getattribute__(self, key)

    def __getattr__(self, key):
        return False

    @classmethod
    def __check_input(cls, key, value):
        if key in cls.__attrs:
            correct_type = cls.__attrs[key]
            if isinstance(value, correct_type):
                return True
            raise TypeError(f'Неверный тип передаваемый в аттрибут {key}.')
        raise AttributeError(f'Аттрибута {key} не существует.')


class Mummies:
    __attrs = {'name': str, 'location': str, 'descr': str}

    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr

    def __setattr__(self, key, value):
        if self.__check_input(key, value):
            object.__setattr__(self, key, value)

    def __getattribute__(self, key):
        return object.__getattribute__(self, key)

    def __getattr__(self, key):
        return False

    @classmethod
    def __check_input(cls, key, value):
        if key in cls.__attrs:
            correct_type = cls.__attrs[key]
            if isinstance(value, correct_type):
                return True
            raise TypeError(f'Неверный тип передаваемый в аттрибут {key}.')
        raise AttributeError(f'Аттрибута {key} не существует.')


class Papyri:
    __attrs = {'name': str, 'date': str, 'descr': str}

    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr

    def __setattr__(self, key, value):
        if self.__check_input(key, value):
            object.__setattr__(self, key, value)

    def __getattribute__(self, key):
        return object.__getattribute__(self, key)

    def __getattr__(self, key):
        return False

    @classmethod
    def __check_input(cls, key, value):
        if key in cls.__attrs:
            correct_type = cls.__attrs[key]
            if isinstance(value, correct_type):
                return True
            raise TypeError(f'Неверный тип передаваемый в аттрибут {key}.')
        raise AttributeError(f'Аттрибута {key} не существует.')


class Museum:
    __attrs = {'name': str, 'exhibits': list, 'exhibit': (Picture,
                                                          Mummies,
                                                          Papyri)}

    def __init__(self, name):
        self.name = name
        self.exhibits = list()

    def __setattr__(self, key, value):
        if self.__check_input(key, value):
            object.__setattr__(self, key, value)

    def __getattribute__(self, key):
        return object.__getattribute__(self, key)

    def __getattr__(self, key):
        return False

    @classmethod
    def __check_input(cls, key, value):
        if key in cls.__attrs:
            correct_type = cls.__attrs[key]
            if isinstance(value, correct_type):
                return True
            raise TypeError(f'Неверный тип передаваемый в аттрибут {key}.')
        raise AttributeError(f'Аттрибута {key} не существует.')

    def add_exhibit(self, obj):
        """Добавление нового экспоната в конец списка exhibits."""
        self.exhibit = obj
        self.exhibits.append(self.exhibit)
        del self.exhibit

    def remove_exhibit(self, obj):
        """Удаление экспоната из списка exhibits со ссылкой exhibit."""
        if obj not in self.exhibits:
            raise ValueError('Такого экспоната нет в списке.')
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        """Получение информации об экспонате (строка) по индексу."""
        if len(self.exhibits) < indx:
            raise IndexError('Список не имеет экспонатов с таким индексом.')
        obj = self.exhibits[indx]
        info = f'Описание экспоната {obj.name}: {obj.descr}'
        return info
