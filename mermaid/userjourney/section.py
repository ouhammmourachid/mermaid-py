from .task import Task


class Section:
    def __init__(self, name: str, tasks: list[Task]) -> None:
        self.name: str = name
        self.tasks: list[Task] = tasks

    def __str__(self) -> str:
        string: str = f'\tsection {self.name}\n'
        for task in self.tasks:
            string += f'{task}\n'
        return string
