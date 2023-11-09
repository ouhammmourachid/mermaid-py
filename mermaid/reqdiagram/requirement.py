from enum import Enum
from typing import Union


class Risk(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'


class VerifyMethod(Enum):
    ANALYSIS = 'Analysis'
    INSPECTION = 'Inspection'
    TEST = 'Test'
    DEMONSTRATION = 'Demonstration'


class Type(Enum):
    REQUIREMENT = 'requirement'
    FUNCTIONAL = 'functionalRequirement'
    INTERFACE = 'interfaceRequirement'
    PERFORMANCE = 'performanceRequirement'
    PHYSICAL = 'physicalRequirement'
    DESIGN_CONSTRAINT = 'designConstraint'


class Requirement:
    def __init__(self, id_: str, name: str, text: str, type_: Union[str, Type],
                 risk: Union[str, Risk],
                 verifymethod: Union[str, VerifyMethod]) -> None:
        self.id_: str = id_
        self.name: str = name
        self.text: str = text
        self.type_: str = type_ if isinstance(type_, str) else type_.value
        self.risk: str = risk if isinstance(risk, str) else risk.value
        self.verifymethod: str = verifymethod if isinstance(
            verifymethod, str) else verifymethod.value

    def __str__(self) -> str:
        string: str = ''
        string += f'{self.type_} {self.name} {{\n'
        string += f'\tid: {self.id_}\n'
        string += f'\ttext: {self.text}\n'
        string += f'\trisk: {self.risk}\n'
        string += f'\tverifymethod: {self.verifymethod}\n'
        string += '}\n'
        return string
