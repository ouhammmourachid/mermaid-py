from typing import Union

from .element import Element
from .requirement import Requirement


class Link:
    def __init__(self, source: Union[Element, Requirement],
                 destination: Union[Element, Requirement], type_: str) -> None:
        self.source: Union[Element, Requirement] = source
        self.destination: Union[Element, Requirement] = destination
        self.type_: str = type_

    def __str__(self) -> str:
        return f'{self.source.name} - {self.type_} -> {self.destination.name}'
