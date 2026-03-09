import base64
import os
from enum import Enum
from pathlib import Path
from typing import Optional, Union
from urllib.parse import urlencode

import requests
from requests import Response

from .graph import Graph


class MermaidError(Exception):
    """
    Custom exception for Mermaid API errors.
    
    Parses error messages from the API response into a more readable form.
    """
    
    def __init__(self, status_code: int, response_text: str, url: str):
        """
        Initialize MermaidError with parsed error information.
        
        Parameters:
            status_code (int): The HTTP status code from the API response.
            response_text (str): The response body from the API.
            url (str): The URL that was requested.
        """
        self.status_code = status_code
        self.response_text = response_text
        self.url = url
        
        # Parse the error message
        readable_message = self._parse_error_message(status_code, response_text)
        super().__init__(readable_message)
    
    @staticmethod
    def _parse_error_message(status_code: int, response_text: str) -> str:
        """
        Parse the error message from the API response into a readable form.
        
        Parameters:
            status_code (int): The HTTP status code.
            response_text (str): The response body.
            
        Returns:
            str: A formatted error message.
        """
        # Build base error message
        error_msg = f"Mermaid API Error [{status_code}]"
        
        # Handle common status codes
        status_messages = {
            400: "Bad Request - Invalid diagram syntax or parameters",
            401: "Unauthorized - Authentication required",
            403: "Forbidden - Access denied",
            404: "Not Found - Endpoint not available",
            500: "Internal Server Error - Service error",
            502: "Bad Gateway - Service unavailable",
            503: "Service Unavailable - Please try again later",
            504: "Gateway Timeout - Request took too long",
        }
        
        if status_code in status_messages:
            error_msg += f": {status_messages[status_code]}"
        else:
            error_msg += f": HTTP {status_code} Error"
        
        # Append response text if available and not too long
        if response_text and len(response_text) < 500:
            error_msg += f"\n\nDetails: {response_text}"
        elif response_text:
            error_msg += f"\n\nDetails: {response_text[:200]}..."
        
        return error_msg


class Position(Enum):
    """
    This class represents the position of the node in a Mermaid diagram.
    """

    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    NONE = "none"


class Mermaid:
    """
    This class represents a Mermaid diagram.

    Attributes:
        _diagram (str): The base64 encoded string of the Mermaid diagram script.
        svg_response (Response): The response from the GET request to the Mermaid SVG API.
        img_response (Response): The response from the GET request to the Mermaid IMG API.
    """

    def __init__(
        self,
        graph: Union[Graph, str],
        width: Optional[int] = None,
        height: Optional[int] = None,
        scale: Optional[float] = None,
        position: Union[Position, str] = Position.NONE,
    ):
        """
        The constructor for the Mermaid class.

        Parameters:
            graph (Graph): The Mermaid diagram. It can be an instance of the Graph class or a string representing the script.
            width (Optional[int]): The width of the SVG image.
            height (Optional[int]): The height of the SVG image.
            scale (Optional[float]): The scale of the SVG image.
                Must be an float between 1 and 3, and one of height or width must be provided.
            position (Union[Position, str]): The position of the node in the Mermaid diagram.
        """
        if scale:
            assert 1 <= scale <= 3, "Scale must be between 1 and 3"
            assert any([width, height]), (
                "One or both of width and height must be provided"
            )

        self.__position: str = position if isinstance(position, str) else position.value
        self.__height = height if height else None
        self.__width = width if width else None
        self.__scale = scale if scale else None

        self._diagram = self._get_encoded_script(
            graph if isinstance(graph, str) else graph.script
        )
        self._make_request_to_mermaid()

    def _build_query_params(self, image_format: Optional[str] = None) -> str:
        """
        Build the query parameters for the Mermaid API request.

        Parameters:
            image_format (Optional[str]): The image format for /img endpoint
        """
        params = {
            param: value
            for param, value in [
                ("width", self.__width),
                ("height", self.__height),
                ("scale", self.__scale),
                ("format", image_format),
            ]
            if value
        }

        return urlencode(params, doseq=True)

    def set_position(self, position: Union[Position, str]) -> None:
        """
        Set the position of the node in the Mermaid diagram.

        Parameters:
            position (Union[Position, str]): The position of the node.
        """
        self.__position = position if isinstance(position, str) else position.value

    @staticmethod
    def _get_encoded_script(script: str) -> str:
        # CRITICAL FIX: Explicit UTF-8 encoding before base64
        script_bytes = script.encode("utf-8")

        # Use URL-safe base64 encoding (replaces + with -, / with _)
        encoded = base64.urlsafe_b64encode(script_bytes).decode("ascii")
        return encoded

    def _repr_html_(self) -> str:
        """
        Return the text of the SVG response.

        Returns:
            str: The text of the SVG response.
        """
        if self.__position == Position.NONE.value:
            return self.svg_response.text
        return (
            f'<div style="text-align:{self.__position}">{self.svg_response.text}</div>'
        )

    def _make_request_to_mermaid(self) -> None:
        """
        Make GET requests to the Mermaid SVG and IMG APIs using
        the base64 encoded string of the Mermaid diagram script.
        
        Raises:
            MermaidError: If the API request fails.
        """
        mermaid_server_adress: str = os.getenv(
            "MERMAID_INK_SERVER", "https://mermaid.ink"
        )

        svg_url = (
            mermaid_server_adress
            + "/svg/"
            + self._diagram
            + "?"
            + self._build_query_params()
        )
        
        img_url = (
            mermaid_server_adress
            + "/img/"
            + self._diagram
            + "?"
            + self._build_query_params(image_format="png")
        )
        
        self.svg_response: Response = requests.get(svg_url)
        if not self.svg_response.ok:
            raise MermaidError(
                self.svg_response.status_code,
                self.svg_response.text,
                svg_url
            )
        
        self.img_response: Response = requests.get(img_url)
        if not self.img_response.ok:
            raise MermaidError(
                self.img_response.status_code,
                self.img_response.text,
                img_url
            )

    def to_svg(self, path: Union[str, Path]) -> None:
        """
        Write the SVG response text to a file.

        Parameters:
            path (Union[str, Path]): The path of the file to write to.
        """
        with open(path, "w", encoding="utf-8") as file:
            file.write(self.svg_response.text)

    def to_png(self, path: Union[str, Path]) -> None:
        """
        Write the IMG response content to a file.

        Parameters:
            path (Union[str, Path]): The path of the file to write to.
        """
        with open(path, "wb") as file:
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
            graph: Graph = Graph("mermaid diagram", script)
            mermaid: Mermaid = Mermaid(graph)
            if "--img" in options:
                display(Image(mermaid.img_response.content))
            else:
                display(Mermaid(graph))

        get_ipython().register_magic_function(mermaidjs, magic_kind="cell")
except ImportError:
    print(
        "Warning: IPython is not installed. Mermaidjs magic function is not available."
    )
