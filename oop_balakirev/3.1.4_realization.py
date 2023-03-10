class Shop:
    __args = {'name': str, 'goods': list}

    def __init__(self, name) -> None:
        self.name = name
        self.goods: list = list()

    @classmethod
    def __check_input(cls, key, value) -> bool:
        """Функция возвращает True если введенный тип данных соответствует типу
        данных хранящихся в аргументе, иначе False
        """
        correct_type = cls.__args[key]
        return isinstance(value, correct_type)

    def add_product(self, product) -> None:
        """Функция добавляет новый товар в магазин (в конец списка goods)."""
        self.goods.append(product)

    def remove_product(self, product) -> None:
        """Функция удаляет товар product из магазина (из списка goods)."""
        if product in self.goods:
            self.goods.remove(product)

    def __setattr__(self, key, value):
        if key not in self.__args:
            raise AttributeError(f'Аттрибута {key} не существует.')
        if not self.__check_input(key, value):
            raise TypeError('Неверный тип присваиваемых данных.')
        object.__setattr__(self, key, value)


class Product:
    __attrs = {
        'id': int, 'name': str,
        'weight': (int, float),
        'price': (int, float)
        }
    __not_negative = ['weight', 'price']
    __block = ['id']
    __id = 0

    def __init__(self, name, weight, price):
        self.id = self.__make_id()
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def __check_input(cls, key, value) -> bool:
        """Функция возвращает True если введенный тип данных соответствует типу
        данных хранящихся в аргументе, иначе False
        """
        correct_type = cls.__attrs[key]
        if key in cls.__not_negative:
            return value >= 0 and isinstance(value, correct_type)
        return isinstance(value, correct_type)

    @classmethod
    def __make_id(cls) -> int:
        """Функция для каждого нового товара делает уникальный ID."""
        cls.__id += 1
        return cls.__id

    def __setattr__(self, key, value):
        if key not in self.__attrs:
            raise AttributeError(f'Аттрибута {key} не существует.')
        elif not self.__check_input(key, value):
            raise TypeError('Неверный тип присваиваемых данных.')
        object.__setattr__(self, key, value)

    def __delattr__(self, key):
        if key in self.__block:
            raise AttributeError(f'Атрибут {key} удалять запрещено.')
        elif key not in self.__attrs:
            raise AttributeError(f'Аттрибута {key} не существует.')
        object.__delattr__(self, key)
