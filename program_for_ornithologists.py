class Bird:
    def __init__(self, name: str, size: str) -> None:
        self.name = name
        self.size = size

    def describe(self, full: bool = False) -> str:
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name: str, size: str, color: str) -> None:
        super().__init__(name, size)
        self.color = color

    def describe(self, full: bool = False) -> str:
        if not full:
            return super().describe(full)
        return (
            f'Попугай {self.name} — заметная птица,'
            f' окрас её перьев — {self.color}, а размер — {self.size}.'
            ' Интересный факт: попугаи чувствуют ритм, а вовсе не бездумно'
            ' двигаются под музыку. Если сменить композицию, то и темп'
            ' движений птицы изменится.')


    def repeat(self, phrase: str) -> str:
        return f'Попугай {self.name} говорит: {phrase}.'


class Penguin(Bird):
    def __init__(self, name: str, size: str, genus: str) -> None:
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full: bool = False) -> str:
        if not full:
            return super().describe(full)
        return (
            f'Размер пингвина {self.name} из рода {self.genus} — {self.size}.'
            ' Интересный факт: однажды группа геологов-разведчиков похитила'
            ' пингвинье яйцо, и их принялась преследовать вся стая, не'
            ' пытаясь, впрочем, при этом нападать. Посовещавшись, похитители'
            ' вернули птицам яйцо, и те отстали.')

    def swimming(self, speed: int = 11) -> str:
        return (
            f'Пингвин {self.name} плавает со средней скоростью {speed} км/ч.')


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')


print(kesha.repeat('Кеша хороший!'))
print(kowalski.swimming())
