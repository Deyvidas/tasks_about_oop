class CorrectInput:
    attrs = {
        '__x': (int, float),
        '__y': (int, float),
        '__radius': (int, float),
        }
    only_positive = ('__radius',)

    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_input(self.name, value)
        setattr(instance, self.name, value)

    @classmethod
    def check_input(cls, key, value):
        if key in cls.attrs:
            correct_type = cls.attrs[key]
            if isinstance(value, correct_type):
                if key in cls.only_positive:
                    if value > 0:
                        return True
                    raise ValueError(f'Attribute {key} can be only positive.')
                return True
            raise TypeError(f'Attribute {key} must be {correct_type}.')
        raise AttributeError(f'Attribute {key} not found.')


class Circle:
    x = CorrectInput()
    y = CorrectInput()
    radius = CorrectInput()

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __getattr__(self, item):
        return False
