import os
import re
from pathlib import Path
from typing import Optional

from .graph import Graph


def load(path: Path) -> Graph:
    script: Optional[str] = None
    name: Optional[str] = None

    if os.path.exists(path):
        with open(path, 'r') as file:
            script = file.read()
    else:
        raise FileNotFoundError(f'could not find a file in path::{path}')

    file_name: str = os.path.basename(path)
    name, _ = os.path.splitext(file_name)

    return Graph(name, script)


def text_to_snake_case(text: str) -> str:
    # Remove non-alphanumeric characters except underscores and replace spaces with underscores
    out: str = re.sub(r'[^a-zA-Z0-9_]', '_', text)

    # Convert the text to lowercase
    out = out.lower()

    return out
