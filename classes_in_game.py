from random import randint

DEFAULT_STAMINA: int = 80
DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10


class Character:
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple = (1, 3)
    RANGE_VALUE_DEFENCE: tuple = (1, 5)
    SPECIAL_BUFF: int = 15
    SPECIAL_SKILL: str = 'Удача'

    def __init__(self, name: str) -> None:
        self.name = name

    def attack(self) -> str:
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс урон противнику равный {value_attack}'

    def defence(self) -> str:
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} урона'

    def special(self) -> str:
        return (f'{self.name} применил специальное умение'
                f' {self.SPECIAL_SKILL} {self.SPECIAL_BUFF}»')

    @staticmethod
    def choice_char_class(char_name: str):
        """Function return a object type subclass of Character"""
        game_classes = {
            'warrior': Warrior,
            'mage': Mage,
            'healer': Healer}
        approve_choice: str = str()
        char_class: str = str()
        while approve_choice != 'y':
            sele_class = input('Введи название персонажа, за которого хочешь'
                               ' играть: Воитель — warrior, Маг — mage, Лекарь'
                               ' — healer: ').lower()
            char_class = game_classes[sele_class](char_name)
            print(char_class)
            approve_choice = input('Нажми (Y), чтобы подтвердить выбор,'
                                   ' или любую другую кнопку,'
                                   ' чтобы выбрать другого персонажа ').lower()
        return char_class

    @staticmethod
    def start_training(character) -> None:
        commands = {
            'attack': character.attack,
            'defence': character.defence,
            'special': character.special}
        command = input('Введи команду: ')
        if command in commands:
            print(commands[command]())

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя.'
                                  ' Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple = (3, 5)
    RANGE_VALUE_DEFENCE: tuple = (5, 10)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' находчивый воин дальнего боя.'
                                  ' Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple = (5, 10)
    RANGE_VALUE_DEFENCE: tuple = (-2, 2)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' могущественный заклинатель.'
                                  ' Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple = (2, 5)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита'
