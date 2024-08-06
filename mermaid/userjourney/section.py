from .task import Task


class Section:
    """Section class.

    This class represents a section in a user's journey.
    Each section contains a list of tasks.

    Attributes:
        name (str): The name of the section.
        tasks (list[Task]): The tasks in the section.
    """

    def __init__(self, name: str, tasks: list[Task]) -> None:
        """Initialize a new Section.

        Args:
            name (str): The name of the section.
            tasks (list[Task]): The tasks in the section.
        """
        self.name: str = name
        self.tasks: list[Task] = tasks

    def __str__(self) -> str:
        """Return a string representation of the section.

        Returns:
            str: A string representation of the section.
        """
        string: str = f"\tsection {self.name}\n"
        for task in self.tasks:
            string += f"{task}\n"
        return string
