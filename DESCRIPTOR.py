class Descriptor:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__check_input(self.name, value):
            setattr(instance, self.name, value)

    @staticmethod
    def __check_input(key, value):
        attrs = {'__real': (int, float), '__img': (int, float)}
        if key in attrs:
            correct_type = attrs[key]
            if isinstance(value, correct_type):
                return True
            raise ValueError("Неверный тип данных.")


class Complex:
    real = Descriptor()
    img = Descriptor()

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __abs__(self):
        return (self.real**2 + self.img**2)**0.5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
