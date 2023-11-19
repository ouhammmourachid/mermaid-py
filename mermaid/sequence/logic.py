from mermaid.sequence.link import Link


class Loop:
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
        return f'\tloop {self.condition}\n' + ''.join(
            [str(link) for link in self.link]) + '\tend\n'


class Alt:
    """Alt class for mermaid sequence diagram.

    Args:
        condition_links (dict[str, List[Link]]): Dictionary of condition and list of Link objects.
    """
    def __init__(self, condition_links: dict[str, list[Link]]):
        """Initialize alt.

        Args:
            condition_links (dict[str, List[Link]]): Dictionary of condition and list of Link objects.
        """
        self.condition_links = condition_links

    def __str__(self) -> str:
        """Return alt string.

        Returns:
            str: Alt string.
        """
        alt_str = ''
        n = 1
        for condition, links in self.condition_links.items():
            if n == 1:
                alt_str += f'\talt {condition}\n'+ ''.join([str(link) for link in links])
                n += 1
            else:
                alt_str += f'\telse {condition}\n'+ ''.join([str(link) for link in links])

        alt_str += '\tend\n'
        return alt_str