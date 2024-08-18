from dataclasses import dataclass


@dataclass
class Actor:
    """Actor class.

    This class represents an actor in a movie or a play.

    Attributes:
        name (str): The name of the actor.
    """

    name: str
