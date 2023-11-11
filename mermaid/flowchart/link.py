from enum import Enum
from typing import Union

from .node import Node

LINK_SHAPES: dict[str, str] = {
    'normal': '--',
    'dotted': '-.-',
    'thick': '==',
    'hiden': '~~~'
}

LINK_HEADS: dict[str, str] = {
    'none': '',
    'arrow': '>',
    'left-arrow': '<',
    'bullet': 'o',
    'cross': 'x',
}


class LinkShape(Enum):
    NORMAL = 'normal'
    DOTTED = 'dotted'
    THICK = 'thick'
    HIDEN = 'hiden'


class LinkHead(Enum):
    NONE = 'none'
    ARROW = 'arrow'
    LEFT_ARROW = 'left-arrow'
    BULLET = 'bullet'
    CROSS = 'cross'


class Link:
    def __init__(self,
                 origin: Node,
                 end: Node,
                 shape: Union[str, LinkShape] = 'normal',
                 head_left: Union[str, LinkHead] = 'none',
                 head_right: Union[str, LinkHead] = 'arrow',
                 message: str = '') -> None:
        self.oigin: Node = origin
        self.end: Node = end
        self.head_left: str = LINK_HEADS[
            head_left if isinstance(head_left, str) else head_left.value]
        self.head_right: str = LINK_HEADS[
            head_right if isinstance(head_right, str) else head_right.value]
        self.shape: str = LINK_SHAPES[shape if isinstance(shape, str
                                                          ) else shape.value]
        self.message: str = f'|{message}|' if message else message

    def __str__(self) -> str:
        if self.message:
            element: list[str] = [
                self.oigin.id_,
                ' ',
                self.head_left,
                self.shape,
                self.head_right,
                self.message,
                ' ',
                self.end.id_,
            ]
        else:
            element = [
                self.oigin.id_,
                ' ',
                self.head_left,
                self.shape,
                self.head_right,
                ' ',
                self.end.id_,
            ]
        return ''.join(element)
