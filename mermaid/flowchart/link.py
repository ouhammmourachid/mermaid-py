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
