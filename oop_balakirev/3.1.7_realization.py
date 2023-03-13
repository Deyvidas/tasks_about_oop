from __future__ import annotations
from dataclasses import dataclass, field


@dataclass(repr=False)
class SmartPhone:
    model: str
    apps: list = field(init=False, default_factory=list)
    app: (AppVK, AppYouTube, AppPhone) = field(init=False)

    def __setattr__(self, key, value):
        if self.check_input(key, value):
            object.__setattr__(self, key, value)

    @classmethod
    def check_input(cls, key, value):
        if key in cls.__annotations__:
            correct_type = eval(cls.__annotations__[key])
            if isinstance(value, correct_type):
                return True
            raise TypeError(f'Type of {key} must be {correct_type}')
        raise AttributeError(f'Attribute {key} is not exist.')

    def add_app(self, app):
        if app not in self.apps:
            self.app = app
            self.apps.append(self.app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


@dataclass(repr=False)
class AppVK:
    name: str = field(init=False, default='ВКонтакте')

    def __setattr__(self, key, value):
        if self.check_input(key, value):
            object.__setattr__(self, key, value)

    @classmethod
    def check_input(cls, key, value):
        if key in cls.__annotations__:
            correct_type = eval(cls.__annotations__[key])
            if isinstance(value, correct_type):
                return True
            raise TypeError(f'Type of {key} must be {correct_type}')
        raise AttributeError(f'Attribute {key} is not exist.')


@dataclass(repr=False)
class AppYouTube:
    name: str = field(init=False, default='YouTube')
    memory_max: int = field(compare=False)

    def __setattr__(self, key, value):
        if self.check_input(key, value):
            object.__setattr__(self, key, value)

    @classmethod
    def check_input(cls, key, value):
        if key in cls.__annotations__:
            correct_type = eval(cls.__annotations__[key])
            if isinstance(value, correct_type):
                return True
            raise TypeError(f'Type of {key} must be {correct_type}')
        raise AttributeError(f'Attribute {key} is not exist.')


@dataclass(repr=False)
class AppPhone:
    name: str = field(init=False, default='Phone')
    phone_list: dict = field(compare=False)

    def __setattr__(self, key, value):
        if self.check_input(key, value):
            object.__setattr__(self, key, value)

    @classmethod
    def check_input(cls, key, value):
        if key in cls.__annotations__:
            correct_type = eval(cls.__annotations__[key])
            if isinstance(value, correct_type):
                return True
            raise TypeError(f'Type of {key} must be {correct_type}')
        raise AttributeError(f'Attribute {key} is not exist.')


phone1 = SmartPhone('model1')
app1 = AppVK()
app2 = AppVK()
app3 = AppYouTube(1024)
app4 = AppYouTube(740)
app5 = AppPhone({"Балакирев": 123456789, "Сергей": 98450647365, "Работа": 112})
app6 = AppPhone({"Балакирев": 123456789, "Сергей": 98450647365, "Работа": 12})
for app in [app1, app2, app3, app4, app5, app6]:
    phone1.add_app(app)