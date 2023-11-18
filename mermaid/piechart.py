"""
This module contains the PieChart class which extends the Graph class
from mermaid.graph module.

The PieChart class represents a PieChart diagram and provides methods
to build the Mermaid diagram script for the pie chart.

Classes:
    PieChart: Represents a PieChart diagram.
"""
from mermaid.graph import Graph


class PieChart(Graph):
    """
    This class represents a PieChart diagram.

    Attributes:
        data (dict[str, float]): The data for the pie chart.
        show_data (bool): Whether to show data on the pie chart.
    """
    def __init__(self,
                 title: str,
                 data: dict[str, float],
                 show_data: bool = False):
        """
        The constructor for the PieChart class.

        Parameters:
            title (str): The title of the pie chart.
            data (dict[str, float]): The data for the pie chart.
            show_data (bool): Whether to show data on the pie chart. Defaults to False.
        """
        super().__init__(title, '')
        self.data: dict[str, float] = data
        self.show_data: bool = show_data
        self._build_script()

    def _build_script(self) -> None:
        """
        Build the Mermaid diagram script for the pie chart.
        """
        super()._build_script()
        showData: str = ' showData' if self.show_data else ''
        script: str = f'\npie{showData}'

        for key, value in self.data.items():
            script += f'\n\t"{key}" : {value}'

        self.script += script + '\n'
