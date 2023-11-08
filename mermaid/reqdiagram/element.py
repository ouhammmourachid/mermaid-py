from typing import Optional


class Element:
    def __init__(self,
                 name: str,
                 type_: str,
                 docRef: Optional[str] = None) -> None:
        self.name: str = name
        self.type_: str = type_
        self.docRef: Optional[str] = docRef

    def __str__(self) -> str:
        string: str = f'element {self.name} {{\n'
        string += f'\ttype: "{self.type_}"\n'
        string += f'\tdocRef: {self.docRef}\n' if self.docRef else ''
        string += '}\n'
        return string
