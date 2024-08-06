from typing import Union

from .actor import Actor


class Task:
    """Task class.

    This class represents a task in a section of a user's journey.

    Attributes:
        name (str): The name of the task.
    """

    def __init__(
        self, name: str, score: int, actors: Union[list[Actor], Actor]
    ) -> None:
        """Initialize a new Task.

        Args:
            name (str): The name of the task.
        """
        self.name: str = name
        self.score: int = score
        self.actors: list[Actor] = actors if isinstance(actors, list) else [actors]

    def __str__(self) -> str:
        """Return a string representation of the task.

        Returns:
            str: A string representation of the task.
        """
        actor_string: str = ", ".join([actor.name for actor in self.actors])
        return f"\t\t{self.name}: {self.score} : {actor_string}"
