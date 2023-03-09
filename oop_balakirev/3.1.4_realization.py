class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.goods: list = list()

    def add_product(self, product) -> None:
        """Функция добавляет новый товар в магазин (в конец списка goods)."""
        self.goods.append(product)

    def remove_product(self, product) -> None:
        """Функция удаляет товар product из магазина (из списка goods)."""
        if product in self.goods:
            self.goods.remove(product)


class Product:
    __ATTRS = {
        'id': int, 'name': str,
        'weight': (int, float),
        'price': (int, float)
        }
    __NOT_NEGATIVE = ['weight', 'price']
    __BLOCK = ['id']
    __ID = 0

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
        correct_type = cls.__ATTRS[key]
        if key in cls.__NOT_NEGATIVE:
            return value >= 0 and isinstance(value, correct_type)
        return isinstance(value, correct_type)

    @classmethod
    def __make_id(cls) -> int:
        """Функция для каждого нового товара делает уникальный ID."""
        cls.__ID += 1
        return cls.__ID

    def __setattr__(self, key, value):
        if key not in self.__ATTRS:
            raise AttributeError(f'Аттрибута {key} не существует.')
        elif not self.__check_input(key, value):
            raise TypeError('Неверный тип присваиваемых данных.')
        object.__setattr__(self, key, value)

    def __delattr__(self, key):
        if key in self.__BLOCK:
            raise AttributeError(f'Атрибут {key} удалять запрещено.')
        elif key not in self.__ATTRS:
            raise AttributeError(f'Аттрибута {key} не существует.')
        object.__delattr__(self, key)
