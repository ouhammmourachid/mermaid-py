import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Graph:
    """Graph is Base Class witch the other class inhirite from like `flowcahrt` , `erDiagram` , etc..

    Graph has two attribure:
    - title: string represent the title of the digrame.
    - script: string that store the main script to create the digram.

    examples:
    >>> from mermaid.graph import Graph
    >>> grph = Graph("title","...")
    """
    title: str
    script: str

    def save(self, path: Optional[Path] = None) -> None:
        file_path: Path = path if path else Path(f'./{self.title}.mmd')
        if file_path.suffix not in ['.mmd', '.mermaid']:
            raise ValueError("File extension must be '.mmd' or '.mermaid'")
        with open(file_path, 'w') as file:
            file.write(self.script)

    def _build_script(self) -> None:
        script: str = f'---\ntitle: {self.title}\n---' + self.script
        self.script = script
