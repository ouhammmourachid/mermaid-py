from typing import Union

from .actor import Actor


class Task:
    def __init__(self, name: str, score: int, actors: Union[list[Actor],
                                                            Actor]) -> None:
        self.name: str = name
        self.score: int = score
        self.actors: list[Actor] = actors if isinstance(actors,
                                                        list) else [actors]

    def __str__(self) -> str:
        actor_string: str = ', '.join([actor.name for actor in self.actors])
        return f'\t\t{self.name}: {self.score} : {actor_string}'
