from enum import Enum
from typing import Union

from mermaid.sequence.element import Actor, Participant

ARROW_TYPES: dict[str, str] = {
    "Solid-line": "->",
    "Dotted-line": "-->",
    "Solid-arrow": "->>",
    "Dotted-arrow": "-->>",
    "Solid-cross": "-x",
    "Dotted-cross": "--x",
    "Solid-async": "-)",
    "Dotted-async": "--)",
}


class ArrowTypes(Enum):
    """Arrow types for mermaid sequence diagram."""

    SOLID_LINE = "->"
    DOTTED_LINE = "-->"
    SOLID_ARROW = "->>"
    DOTTED_ARROW = "-->>"
    SOLID_CROSS = "-x"
    DOTTED_CROSS = "--x"
    SOLID_ASYNC = "-)"
    DOTTED_ASYNC = "--)"


class Link:
    """Link class for mermaid sequence diagram.

    Args:
        source (ActorParticipant): Source of the link.
        target (ActorParticipant): Target of the link.
        type_ (Union[str,ArrowTypes]): Type of the link.
        message (str): Message to be displayed over the link.
        activate_target (bool, optional): Activate the target. Defaults to False.
        deactivate_target (bool, optional): Deactivate the target. Defaults to False.

    """

    def __init__(
        self,
        source: Union[Actor, Participant],
        target: Union[Actor, Participant],
        type_: Union[str, ArrowTypes],
        message: str,
        activate_target: bool = False,
        deactivate_target: bool = False,
    ) -> None:
        self.source: Union[Actor, Participant] = source
        self.target: Union[Actor, Participant] = target
        self.type_: Union[str, ArrowTypes] = (
            ARROW_TYPES[type_] if isinstance(type_, str) else type_.value
        )
        self.activate_target: bool = activate_target
        self.deactivate_target: bool = deactivate_target
        self.message: str = message

    def __str__(self) -> str:
        string: str = (
            f"\t{self.source.id_}{self.type_}{self.target.id_}: {self.message}\n"
        )
        if self.activate_target:
            string += f"activate {self.target.id_}\n"
        if self.deactivate_target:
            string += f"deactivate {self.target.id_}\n"

        return string
