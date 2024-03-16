"""Graph module.

This module provides the Graph base class for creating and manipulating
different types of diagrams such as flowcharts, ER diagrams, etc.

Classes:
    Graph: Represents a base class for different types of diagrams.
"""
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Graph:
    """Graph base class.

    This class serves as a base for other classes representing different
    types of diagrams like `Flowchart`, `ERDiagram`, etc.

    Attributes:
        title (str): The title of the diagram.
        script (str): The main script to create the diagram.
    """
    title: str
    script: str

    def save(self, path: Optional[Path] = None) -> None:
        """Save the diagram to a file.

        Args:
            path (Optional[Path]): The path to save the diagram. If not
                provided, the diagram will be saved in the current directory
                with the title as the filename.
        Raises:
            ValueError: If the file extension is not '.mmd' or '.mermaid'.
        """
        file_path: Path = path if path else Path(f'./{self.title}.mmd')
        if file_path.suffix not in ['.mmd', '.mermaid']:
            raise ValueError("File extension must be '.mmd' or '.mermaid'")
        with open(file_path, 'w') as file:
            file.write(self.script)

    def _build_script(self) -> None:
        script: str = f'---\ntitle: {self.title}\n---' + self.script
        self.script = script
