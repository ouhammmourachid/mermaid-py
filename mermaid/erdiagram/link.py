from .entity import Entity

LIST_CARDINALITIES: dict[str, list[str]] = {
    'zero-or-one': ['|o', 'o|'],
    'exactly-one': ['||', '||'],
    'zero-or-more': ['}o', 'o{'],
    'one-or-more': ['}|', '|{'],
}


class Link:
    def __init__(self,
                 origin: Entity,
                 end: Entity,
                 origin_cardinality: str,
                 end_cardinality: str,
                 label: str = '',
                 dotted: bool = False) -> None:
        self.origin: Entity = origin
        self.end: Entity = end
        self.label: str = label
        self.left_symbol: str = LIST_CARDINALITIES[origin_cardinality][0]
        self.right_symbol: str = LIST_CARDINALITIES[end_cardinality][1]
        self.dotted: bool = dotted

    def __str__(self) -> str:
        shape: str = '..' if self.dotted else '--'
        return f'{self.origin.name}{self.left_symbol}{shape}{self.right_symbol}{self.end.name} : "{self.label}"'
