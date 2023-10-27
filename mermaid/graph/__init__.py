import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Graph:
    title: str
    script: str

    def save(self, path: Optional[Path] = None) -> None:
        file_path: Path = path if path else Path(f'./{self.title}.txt')

        with open(file_path, 'w') as file:
            file.write(self.script)
