from typing import Union

from mermaid.sequence.link import Link


class Logic:
    """Logic class for mermaid sequence diagram."""

    pass


class Loop(Logic):
    """Loop class for mermaid sequence diagram.

    Args:
        condition (str): Condition of the loop.
        link (List[Link]): List of Link objects.
    """

    def __init__(self, condition: str, link: list[Link]):
        """Initialize loop.

        Args:
            condition (str): Condition of the loop.
            link (List[Link]): List of Link objects.
        """
        self.condition = condition
        self.link = link

    def __str__(self) -> str:
        """Return loop string.

        Returns:
            str: Loop string.
        """
        return (
            f"\tloop {self.condition}\n"
            + "".join([str(link) for link in self.link])
            + "\tend\n"
        )


class Alt(Logic):
    """Alt class for mermaid sequence diagram.

    Args:
        condition_links (dict[str, List[Link]]): Dictionary of condition
        and list of Link objects.
    """

    def __init__(self, condition_links: dict[str, list[Link]]):
        """Initialize alt.

        Args:
            condition_links (dict[str, List[Link]]): Dictionary of condition
            and list of Link objects.
        """
        self.condition_links = condition_links

    def __str__(self) -> str:
        """Return alt string.

        Returns:
            str: Alt string.
        """
        alt_str = ""
        n = 1
        for condition, links in self.condition_links.items():
            if n == 1:
                alt_str += f"\talt {condition}\n" + "".join(
                    [str(link) for link in links]
                )
                n += 1
            else:
                alt_str += f"\telse {condition}\n" + "".join(
                    [str(link) for link in links]
                )

        alt_str += "\tend\n"
        return alt_str


class Optional(Logic):
    """Optional class for mermaid sequence diagram.

    Args:
        condition (str): Condition of the loop.
        statements (List[Link]): List of Link objects.
    """

    def __init__(self, condition: str, statements: list[Link]) -> None:
        """Initialize loop.

        Args:
            condition (str): Condition of the loop.
            statements (List[Link]): List of Link objects.
        """
        self.condition = condition
        self.statements = statements

    def __str__(self) -> str:
        """Return loop string.

        Returns:
            str: Loop string.
        """
        return (
            f"\topt {self.condition}\n"
            + "".join([str(statement) for statement in self.statements])
            + "\tend\n"
        )


class Parallel:
    """Parallel class for mermaid sequence diagram.

    Args:
        condition_elements (dict[str, list[Union[Link, Logic]]]): Dictionary of
        condition and Link or Logic objects.
    """

    def __init__(self, condition_elements: dict[str, list[Union[Link, Logic]]]) -> None:
        """Initialize parallel.

        Args:
            condition_elements (dict[str, list[Union[Link, Logic]]]): Dictionary of
            condition and Link or Logic objects.
        """
        self.condition_elements = condition_elements

    def __str__(self) -> str:
        """Return parallel string.

        Returns:
            str: Parallel string.
        """
        parallel_str = ""
        n = 1
        for condition, elements in self.condition_elements.items():
            if n == 1:
                parallel_str += f"\tpar {condition}\n" + "".join(
                    [str(element) for element in elements]
                )
                n += 1
            else:
                parallel_str += f"\tand {condition}\n" + "".join(
                    [str(element) for element in elements]
                )
        parallel_str += "\tend\n"
        return parallel_str


class Critical(Logic):
    """Critical class for mermaid sequence diagram.

    Args:
        condition (str): Condition of the loop.
        link (List[Link]): List of Link objects.
    """

    def __init__(
        self,
        condition: str,
        statements: list[Union[Link, Logic]],
        optional_statements: dict[str, list[Union[Link, Logic]]],
    ) -> None:
        """Initialize loop.

        Args:
            condition (str): Condition of the loop.
            link (List[Link]): List of Link objects.
        """
        self.condition = condition
        self.statements = statements
        self.optional_statements = optional_statements

    def __str__(self) -> str:
        """Return loop string.

        Returns:
            str: Loop string.
        """
        critical_str = f"\tcritical {self.condition}\n" + "".join(
            [str(statement) for statement in self.statements]
        )
        for condition, statements in self.optional_statements.items():
            critical_str += f"\toption {condition}\n" + "".join(
                [str(statement) for statement in statements]
            )
        critical_str += "\tend\n"
        return critical_str


class Break(Logic):
    """Break class for mermaid sequence diagram.

    Args:
        condition (str): Condition of the loop.
        link (List[Link]): List of Link objects.
    """

    def __init__(self, condition: str, statements: list[Union[Link, Logic]]) -> None:
        """Initialize loop.

        Args:
            condition (str): Condition of the loop.
            link (List[Link]): List of Link objects.
        """
        self.condition = condition
        self.statements = statements

    def __str__(self) -> str:
        """Return loop string.

        Returns:
            str: Loop string.
        """
        break_str = f"\tbreak {self.condition}\n" + "".join(
            [str(statement) for statement in self.statements]
        )
        break_str += "\tend\n"
        return break_str
