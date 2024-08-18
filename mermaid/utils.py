import os
import re
from pathlib import Path
from typing import Optional

from .graph import Graph


def load(path: Path) -> Graph:
    """
    Load a Mermaid diagram script from a file and return a Graph object.

    Parameters:
        path (Path): The path of the file to load from.

    Returns:
        Graph: The Graph object containing the Mermaid diagram script and the name of the file.
    """
    script: Optional[str] = None
    name: Optional[str] = None

    if os.path.exists(path):
        with open(path, "r") as file:
            script = file.read()
    else:
        raise FileNotFoundError(f"could not find a file in path::{path}")

    file_name: str = os.path.basename(path)
    name, _ = os.path.splitext(file_name)

    return Graph(name, script)


def text_to_snake_case(text: str) -> str:
    """
    Convert a string to snake_case.

    Parameters:
        text (str): The string to convert.

    Returns:
        str: The converted string.
    """
    # Remove non-alphanumeric characters except underscores, dots and dashes
    #  and replace everything else with underscores
    out: str = re.sub(r"[^a-zA-Z0-9_\.-]", "_", text)

    # Convert the text to lowercase
    out = out.lower()

    return out
