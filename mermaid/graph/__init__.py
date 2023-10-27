import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Graph:
    title: str
    script: str

    def save(self, path: Path | None = None) -> None:
        file_path: Path = path if path else Path(f'./{self.title}.txt')

        with open(file_path, 'w') as file:
            file.write(self.script)

    def _build_script(self) -> None:
        script: str = f'---\ntitle: {self.title}\n---' + self.script
        self.script = script
