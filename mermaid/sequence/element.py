from dataclasses import dataclass

from mermaid._utils import text_to_snake_case


@dataclass
class Actor:
    name: str

    def __str__(self):
        return f'\tActor {self.name}\n'


@dataclass
class Participant:
    name: str

    def __str__(self):
        self.id = text_to_snake_case(self.name)
        return f'\tparticipant {self.id} as {self.name}\n'
