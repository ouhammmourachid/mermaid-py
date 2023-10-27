from typing import Dict, List

from .node import Node

LINK_SHAPES: Dict[str, str] = {
    'normal': '---',
    'dotted': '-.-',
    'thick': '===',
}

LINK_HEADS: Dict[str, str] = {
    'none': '',
    'arrow': '>',
    'left-arrow': '<',
    'bullet': 'o',
    'cross': 'x',
}


class Link:
    def __init__(self,
                 origin: Node,
                 end: Node,
                 shape: str = 'normal',
                 head_left: str = 'none',
                 head_right: str = 'arrow',
                 message: str = '') -> None:
        self.oigin: Node = origin
        self.end: Node = end
        self.head_left = LINK_HEADS[head_left]
        self.head_right = LINK_HEADS[head_right]
        self.shape = LINK_SHAPES[shape]
        self.message = f'|{message}|' if message else message

    def __str__(self) -> str:
        element: List[str] = [
            self.oigin.id_,
            ' ',
            self.head_left,
            self.shape,
            self.message,
            self.shape,
            self.head_right,
            ' ',
            self.end.id_,
        ]
        return ''.join(element)
