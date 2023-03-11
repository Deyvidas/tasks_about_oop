from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Market:
    name: str
    goods: list[None, Good] = field(init=False, default_factory=list)


@dataclass
class Good:
    name: str
    price: float
    weight: float


market = Market('market1')

print(market.__annotations__)  # {'name': 'str', 'goods': 'list[None, Good]'}

for key, value in market.__annotations__.items():
    market.__annotations__[key] = eval(value)

print(market.__annotations__)  # {'name': <class 'str'>, 'goods': list[None, __main__.Good]}