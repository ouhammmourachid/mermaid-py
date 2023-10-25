import os
from pathlib import Path

from .graph import Graph


def read_file(path: Path) -> Graph:
    script: str = None
    name: str = None

    if os.path.exists(path):
        with open(path, 'r') as file:
            script = file.read()
    else:
        raise FileNotFoundError(f'could not find a file in path::{path}')

    file_name: str = os.path.basename(path)
    name, _ = os.path.splitext(file_name)

    return Graph(name, script)
