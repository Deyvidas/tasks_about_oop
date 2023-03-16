class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    def __setattr__(self, key, value):
        key_check = key.split('__')[-1]
        if self.__check_input(key_check, value):
            object.__setattr__(self, key, value)

    def __abs__(self):
        return (self.real**2 + self.img**2)**0.5

    @staticmethod
    def __check_input(key, value):
        attrs = {'real': (int, float), 'img': (int, float)}
        if key in attrs:
            correct_type = attrs[key]
            if isinstance(value, correct_type):
                return True
            raise ValueError("Неверный тип данных.")

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = value


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
