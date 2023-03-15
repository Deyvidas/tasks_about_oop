from functools import wraps

# В decorator_without_param передается ссылка на декорируемую функцию.
def decorator_without_param(*args, **kwargs):
    # args = (<function function at 0x00000220D56EB670>,)
    # kwargs = {}
    func, *other_args = args
    # Что бы не изненять свойства декорированной функции (from functools import wraps)
    @wraps(func)
    # В wrapper передаются аргументы декорируемой функции.
    def wrapper(*args, **kwargs):
        # args = ('string1', 'string2')
        # kwargs = {'str3': 'string3', 'str4': 'string4'}
        print('Декоратор что то делает перед вызовом декорированной функции.')
        result = func(*args, **kwargs)
        print(f'Декоратор распечатал результат декорируемой функции --> {result}')
        print('Декоратор что то делает после вызова декорированной функции.')
        return result
    return wrapper


@decorator_without_param
def function(string1, string2, str3, str4):
    """Documentation of function."""
    return string1, string2, str3, str4


function('string1', 'string2', str3='string3', str4='string4')
print('\n'*3)
# Декоратор что то делает перед вызовом декорированной функции.
# Декоратор распечатал результат декорируемой функции --> ('string1', 'string2', 'string3', 'string4')
# Декоратор что то делает после вызова декорированной функции.


# В decorator_with_param передаются параметры класса декоратора.
def decorator_with_param(*args, **kwargs):
    # args = ('param1', 'param2')
    # kwargs = {'parameter3': 'param3', 'parameter4': 'param4'}
    param1, param2, *other_args = args
    param3, param4, *other_kwargs = kwargs.values()
    # В get_func передается ссылка на декорируемую функцию.
    def get_func(*args, **kwargs):
        # args = (<function function at 0x000001C95974B790>,)
        # kwargs = {}
        func, *other_args = args
        # Что бы не изненять свойства декорированной функции (from functools import wraps)
        @wraps(func)
        # В wrapper передаются аргументы декорируемой функции.
        def wrapper(*args, **kwargs):
            # args = ('string1', 'string2')
            # kwargs =  {'str3': 'string3', 'str4': 'string4'}
            print('Декоратор что то делает перед вызовом декорированной функции.')
            result = func(*args, **kwargs)
            print(f'Декоратор распечатал результат декорируемой функции --> {result}')
            print(f'Декоратор распечатал свои параметры --> {param1, param2, param3, param4}')
            print('Декоратор что то делает после вызова декорированной функции.')
        return wrapper
    return get_func


@decorator_with_param('param1', 'param2', parameter3='param3', parameter4='param4')
def function(string1, string2, str3, str4):
    """Documentation of function."""
    return string1, string2, str3, str4


function('string1', 'string2', str3='string3', str4='string4')
print('\n'*3)
# Декоратор что то делает перед вызовом декорированной функции.
# Декоратор распечатал результат декорируемой функции --> ('string1', 'string2', 'string3', 'string4')
# Декоратор распечатал свои параметры --> ('param1', 'param2', 'param3', 'param4')
# Декоратор что то делает после вызова декорированной функции.


class DecoratorWithoutParams:
    # В __init__ передается ссылка на декорируемую функцию.
    def __init__(self, *args, **kwargs):
        # args = (<function function at ...>,),
        # kwargs = {}
        self.func, *self.other = args

    # В __call__ передаются аргументы декорируемой функции.
    def __call__(self, *args, **kwargs):
        # args = ('string1', 'string2'),
        # kwargs =  {'str3': 'string3', 'str4': 'string4'}
        print('Декоратор что то делает перед вызовом декорированной функции.')
        result = self.func(*args, **kwargs)
        print(f'Декоратор распечатал результат декорируемой функции --> {result}')
        print('Декоратор что то делает после вызова декорированной функции.')
        # Что бы не изненять свойства декорированной функции
        self.__class__.__name__ = self.func.__name__
        self.__class__.__doc__ = self.func.__doc__
        return result


@DecoratorWithoutParams
def function(string1, string2, str3, str4):
    """Documentation of function."""
    return string1, string2, str3, str4


function('string1', 'string2', str3='string3', str4='string4')
print('\n'*3)
# Декоратор что то делает перед вызовом декорированной функции.
# Декоратор распечатал результат декорируемой функции --> ('string1', 'string2', 'string3', 'string4')
# Декоратор что то делает после вызова декорированной функции.


class DecoratorWithParams:
    # В __init__ передаются параметры класса декоратора.
    def __init__(self, *args, **kwargs):
        # args = ('param1', 'param2'),
        # kwargs = {'parameter3': 'param3', 'parameter4': 'param4'}
        self.param1, self.param2, *self.other_args = args
        self.param3, self.param4, *self.other_kwargs = kwargs.values()

    # В __call__ передается ссылка на декорируемую функцию.
    def __call__(self, *args, **kwargs):
        # args = (<function function at 0x000001E19DC7A940>,),
        # kwargs = {}
        self.func, *self.other = args
        # Что бы не изненять свойства декорированной функции (from functools import wraps)
        @wraps(self.func)
        # В wrapper передаются аргументы декорируемой функции.
        def wrapper(*args, **kwargs):
            # args = ('string1', 'string2'),
            # kwargs = {'str3': 'string3', 'str4': 'string4'}
            print('Декоратор что то делает перед вызовом декорированной функции.')
            result = self.func(*args, **kwargs)
            print(f'Декоратор распечатал результат декорируемой функции --> {result}')
            print(f'Декоратор распечатал свои параметры --> {self.param1, self.param2, self.param3, self.param4}')
            print('Декоратор что то делает после вызова декорированной функции.')
            return result
        return wrapper


@DecoratorWithParams('param1', 'param2', parameter3='param3', parameter4='param4')
def function(string1, string2, str3, str4):
    """Documentation of function."""
    return string1, string2, str3, str4


function('string1', 'string2', str3='string3', str4='string4')
print('\n'*3)
# Декоратор что то делает перед вызовом декорированной функции.
# Декоратор распечатал результат декорируемой функции --> ('string1', 'string2', 'string3', 'string4')
# Декоратор распечатал свои параметры --> ('param1', 'param2', 'param3', 'param4')
# Декоратор что то делает после вызова декорированной функции.
