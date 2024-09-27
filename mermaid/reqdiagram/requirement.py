from enum import Enum
from typing import Union


class Risk(Enum):
    """Risk Enum.

    This enum represents the different levels of risk associated with a requirement in a requirement diagram.
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class VerifyMethod(Enum):
    """VerifyMethod Enum.

    This enum represents the different methods of verifying a requirement in a requirement diagram.
    """

    ANALYSIS = "Analysis"
    INSPECTION = "Inspection"
    TEST = "Test"
    DEMONSTRATION = "Demonstration"


class Type(Enum):
    """Return a string representation of the link.

    Returns:
        str: A string representation of the link.
    """

    REQUIREMENT = "requirement"
    FUNCTIONAL = "functionalRequirement"
    INTERFACE = "interfaceRequirement"
    PERFORMANCE = "performanceRequirement"
    PHYSICAL = "physicalRequirement"
    DESIGN_CONSTRAINT = "designConstraint"


class Requirement:
    """Requirement class.

    This class represents a requirement in a requirement diagram.

    Attributes:
        id_ (str): The ID of the requirement.
        name (str): The name of the requirement.
        text (str): The text of the requirement.
        type_ (Union[str, Type]): The type of the requirement.
        risk (Union[str, Risk]): The risk of the requirement.
        verifymethod (Union[str, VerifyMethod]): The verification method of the requirement.
    """

    def __init__(
        self,
        id_: str,
        name: str,
        text: str,
        type_: Union[str, Type],
        risk: Union[str, Risk],
        verifymethod: Union[str, VerifyMethod],
    ) -> None:
        """Initialize a new Requirement.

        Args:
            id_ (str): The ID of the requirement.
            name (str): The name of the requirement.
            text (str): The text of the requirement.
            type_ (Union[str, Type]): The type of the requirement.
            risk (Union[str, Risk]): The risk of the requirement.
            verifymethod (Union[str, VerifyMethod]): The verification method of the requirement.
        """
        self.id_: str = id_
        self.name: str = name
        self.text: str = text
        self.type_: str = type_ if isinstance(type_, str) else type_.value
        self.risk: str = risk if isinstance(risk, str) else risk.value
        self.verifymethod: str = (
            verifymethod if isinstance(verifymethod, str) else verifymethod.value
        )

    def __str__(self) -> str:
        return "".join(
            [
                f"{self.type_} {self.name} {{\n",
                f"\tid: {self.id_}\n",
                f"\ttext: {self.text}\n",
                f"\trisk: {self.risk}\n",
                f"\tverifymethod: {self.verifymethod}\n",
                "}\n",
            ]
        )
