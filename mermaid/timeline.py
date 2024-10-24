"""
This module contains the Timeline class which extends the Graph class
from mermaid.graph module.

The Timeline class represents a Timeline diagram and provides methods
to build the Mermaid diagram script for the timeline.

Classes:
    Timeline: Represents a Timeline diagram.
"""

from typing import Optional, List, Dict

from mermaid.configuration import Config
from mermaid.graph import Graph


class Timeline(Graph):
    """
    This class represents a Timeline diagram.

    Attributes:
        events (List[Dict[str, str]]): The events for the timeline.
        config (Config): The configuration for the timeline.
    """

    def __init__(
        self,
        title: str,
        events: List[Dict[str, str]],
        config: Optional[Config] = None,
    ) -> None:
        """
        The constructor for the Timeline class.

        Parameters:
            title (str): The title of the timeline.
            events (List[Dict[str, str]]): The events for the timeline.
            config (Optional[Config]): The configuration for the timeline. Defaults to None.
        """
        super().__init__(title, "", config)
        self.events: List[Dict[str, str]] = events
        self._build_script()

    def _build_script(self) -> None:
        """
        Build the Mermaid diagram script for the timeline.
        """
        super()._build_script()
        script: str = "\ntimeline"

        for event in self.events:
            date = event["date"]
            descriptions = event["description"].split(" : ")
            for description in descriptions:
                script += f"\n\t{date} : {description}"

        self.script += script + "\n"
