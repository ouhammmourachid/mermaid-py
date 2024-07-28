import base64
from enum import Enum
from pathlib import Path
from typing import Union

import requests
from requests import Response

from .graph import Graph


class Position(Enum):
    """
    Position class
    =================

    This class is an enumeration of the possible positions of the node in the Mermaid diagram.
    """
    LEFT = 'left'
    RIGHT = 'right'
    CENTER = 'center'
    NONE = 'none'


class Mermaid:
    """
    Mermaid class
    =================

    This class call the Mermaid API to render the Mermaid diagram script
    into SVG and IMG formats.

    Attributes:
    ------------

    _diagram : str
        The base64 encoded string of the Mermaid diagram script.
    __position : str
        The position of the node in the Mermaid diagram.
    svg_response : Response
        The response object of the GET request to the Mermaid SVG API.
    img_response : Response
        The response object of the GET request to the Mermaid IMG API.
    
    Methods:
    --------

    set_position(position: Union[Position, str]):
        Set the position of the node in the Mermaid diagram.
    to_svg(path: Union[str, Path]):
        Write the SVG response text to a file.
    to_png(path: Union[str, Path]):
        Write the IMG response content to a file.
    
    Example:
    --------

    >>> from mermaid import Graph, Mermaid
    >>> graph = Graph('graph TD\\nA-->B')
    >>> # Create a Mermaid object
    >>> mermaid = Mermaid(graph)
    >>> # save the SVG response to a file
    >>> mermaid.to_svg('./mermaid.svg')

    """
    def __init__(self,
                 graph: Graph,
                 position: Union[Position, str] = Position.NONE):
        """
        Initialize the Mermaid object.

        Parameters:
        -----------
        graph : Graph
            The Mermaid graph object.
        position : Union[Position, str]
            The position of the node in the Mermaid diagram.
        
        Raises:
        -------
        TypeError:
            If the position is not a string or an instance of the Position enum.
        
        Examples:
        ---------
        >>> from mermaid import Graph, Mermaid, Position
        >>> graph = Graph('graph TD\\nA-->B')
        >>> # Create a Mermaid object without a position
        >>> mermaid = Mermaid(graph)
        >>> # Create a Mermaid object with a position
        >>> mermaid = Mermaid(graph, Position.LEFT)
        
        """
        self.__position: str = position if isinstance(position,
                                                      str) else position.value
        self._diagram = self._process_diagram(graph.script)
        self._make_request_to_mermaid()

    def set_position(self, position: Union[Position, str]) -> None:
        """
        Set the position of the node in the Mermaid diagram.

        Parameters:
        -----------
        position : Union[Position, str]
            The position of the node in the Mermaid diagram.
        
        Raises:
        -------
        TypeError:
            If the position is not a string or an instance of the Position enum.
        
        Example:
        --------
        >>> from mermaid import Graph, Mermaid
        >>> graph = Graph('graph TD\\nA-->B')
        >>> # Create a Mermaid object
        >>> mermaid = Mermaid(graph)
        >>> # Set the position of the node in the Mermaid diagram
        >>> mermaid.set_position('left')
        """
        self.__position = position if isinstance(position,
                                                 str) else position.value

    @staticmethod
    def _process_diagram(diagram: str) -> str:
        """
        Process the Mermaid diagram script into a base64 encoded string.

        Parameters:
            diagram (str): The Mermaid diagram script.

        Returns:
            str: The base64 encoded string of the Mermaid diagram script.
        """
        graphbytes = diagram.encode('utf8')
        base64_bytes = base64.b64encode(graphbytes)
        diagram = base64_bytes.decode('ascii')
        return diagram

    def _repr_html_(self) -> str:
        """
        Return the text of the SVG response.

        Returns:
            str: The text of the SVG response.
        """
        if self.__position == Position.NONE.value:
            return self.svg_response.text
        return f'<div style="text-align:{self.__position}">{self.svg_response.text}</div>'

    def _make_request_to_mermaid(self) -> None:
        """
        Make GET requests to the Mermaid SVG and IMG APIs using
        the base64 encoded string of the Mermaid diagram script.
        """
        self.svg_response: Response = requests.get('https://mermaid.ink/svg/' +
                                                   self._diagram)
        self.img_response: Response = requests.get('https://mermaid.ink/img/' +
                                                   self._diagram)

    def to_svg(self, path: Union[str, Path]) -> None:
        """
        Write the SVG response text to a file.

        Parameters:
        -----------

        path : Path or str
            The path of the file to write to.
        
        Example:
        --------
        >>> from mermaid import Graph, Mermaid
        >>> mermaid = Mermaid(Graph('graph TD\\nA-->B'))
        >>> # Save the SVG response to a file
        >>> mermaid.to_svg('./mermaid.svg')
        """
        with open(path, 'w', encoding='utf-8') as file:
            file.write(self.svg_response.text)

    def to_png(self, path: Union[str, Path]) -> None:
        """
        Write the IMG response content to a file.

        Parameters:
        -----------
        path : Path or str
            The path of the file to write to.
        
        Example:
        --------
        >>> from mermaid import Graph, Mermaid
        >>> mermaid = Mermaid(Graph('graph TD\\nA-->B'))
        >>> # Save the IMG response to a file
        >>> mermaid.to_png('./mermaid.png')
        """
        with open(path, 'wb') as file:
            file.write(self.img_response.content)


try:
    from IPython import get_ipython
    if get_ipython() is not None:
        from IPython.core.magic import register_cell_magic
        from IPython.display import Image, display

        @register_cell_magic
        def mermaidjs(line, cell):
            options = line.strip().split()
            script: str = cell.strip()
            graph: Graph = Graph('mermaid diagram', script)
            mermaid: Mermaid = Mermaid(graph)
            if '--img' in options:
                display(Image(mermaid.img_response.content))
            else:
                display(Mermaid(graph))

        get_ipython().register_magic_function(mermaidjs, magic_kind='cell')
except ImportError:
    # TODO: add a suitible handler for exception.
    print('Error acured while importing mermaidjs .')
