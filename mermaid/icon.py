from dataclasses import dataclass


@dataclass
class Icon:
    name: str
    type_: str
    str_: str = 'v1'

    def __str__(self) -> str:
        if self.str_ == 'v1':
            return f'{self.type_} {self.name}'
        elif self.str_ == 'v2':
            return f'{self.type_} {self.name}'
        return f' {self.type_}:{self.name} '
