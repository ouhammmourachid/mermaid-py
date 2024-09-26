from dataclasses import dataclass
from typing import Optional


@dataclass
class Style:
    """Style class.

    This class represents a style definition for a Mermaid diagram.

    Attributes:
        name (str): The name of the style definition.
        fill (str): The fill color of the style definition.
        color (str): The text color of the style definition.
        font_weight (str): The font weight of the style definition.
        stroke_width (str): The stroke width of the style definition.
        stroke (str): The stroke color of the style definition.
        other (str): Any other style definition separated by ,.
    """

    name: str
    fill: Optional[str] = None
    color: Optional[str] = None
    font_weight: Optional[str] = None
    stroke_width: Optional[str] = None
    stroke: Optional[str] = None
    other: Optional[str] = None

    def __str__(self) -> str:
        """Return the string representation of the style definition."""
        string: str = f"classDef {self.name} "
        string += "".join(
            [
                f",{style}:{value}"
                for style, value in [
                    ("fill", self.fill),
                    ("color", self.color),
                    ("font-weight", self.font_weight),
                    ("stroke-width", self.stroke_width),
                    ("stroke", self.stroke),
                ]
                if value is not None
            ]
        )
        if self.other:
            string += f",{self.other}"
        return string

    def __hash__(self) -> int:
        return hash(self.name)
