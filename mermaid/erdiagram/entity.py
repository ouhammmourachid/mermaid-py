from typing import Optional, Union


class Entity:
    """Entity class.

    This class represents an entity in an ER diagram.

    Attributes:
        name (str): The name of the entity.
        attributes (list[str]): The attributes of the entity.
    """

    def __init__(
        self, name: str, attributes: Optional[dict[str, Union[list[str], str]]] = None
    ) -> None:
        """Initialize a new Entity.

        Args:
            name (str): The name of the entity.
            attributes (Optional[dict[str, Union[list[str], str]]]): The attributes of the entity.
        """
        self.name: str = name
        self.attributes: dict[str, Union[list[str], str]] = (
            attributes if attributes is not None else {}
        )

    def __str__(self) -> str:
        string_attributes: str = self.build_attributes()
        string: str = "".join([self.name, "{\n", string_attributes, "}"])
        return string

    def update_attributes(self, attributes: dict[str, str]) -> None:
        """Update the attributes of the entity.

        Args:
            attributes (dict[str, Union[list[str], str]]): The new attributes of the entity.
        """
        self.attributes.update(attributes)

    def add_attribute(
        self,
        name: str,
        type_: str,
        constraint: Optional[str] = None,
        comment: Optional[str] = None,
    ) -> None:
        """Add an attribute to the entity.

        Args:
            name (str): The name of the attribute.
            attribute_def (Union[list[str], str]): The definition of the attribute.
        """
        attribute_def: list[str] = [type_]
        if constraint is not None:
            attribute_def.append(constraint)
        if comment is not None:
            attribute_def.append(comment)
        self.attributes[name] = attribute_def

    def build_attributes(self) -> str:
        """Build the string representation of the attributes.

        Returns:
            str: The string representation of the attributes.
        """
        string_attributes: str = ""
        for att_name, att_def in self.attributes.items():
            string: str = ""
            if isinstance(att_def, str):
                string = f"\t{att_def} {att_name}\n"
            else:
                if len(att_def) == 1:
                    string = f"{att_def[0]} {att_name}\n"
                elif len(att_def) == 2:
                    if att_def[1] in ["PK", "FK", "UK"]:
                        string = f"\t{att_def[0]} {att_name} {att_def[1]}\n"
                    else:
                        string = f'\t{att_def[0]} {att_name} "{att_def[1]}"\n'
                else:
                    string = f'\t{att_def[0]} {att_name} {att_def[1]} "{att_def[2]}"\n'
            string_attributes += string
        return string_attributes
