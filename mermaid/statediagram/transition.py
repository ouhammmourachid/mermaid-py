from typing import Optional

from mermaid import text_to_snake_case

from .base import BaseTransition
from .state import End, Start, State


class Transition(BaseTransition):
    """Transition class.

    This class represents a transition in a state diagram.

    Attributes:
        from_state (State): The state from which the transition starts.
        to_state (State): The state to which the transition ends.
        label (str): The label of the transition.
    """

    def __init__(
        self, from_: Optional[State] = None, to: Optional[State] = None, label: str = ""
    ) -> None:
        """Initialize a new Transition.

        Args:
            from_ (State): The state from which the transition starts.
            to (State): The state to which the transition ends.
            label (str): The label of the transition.
        """
        if from_ is None:
            from_ = Start()
        if to is None:
            to = End()
        self.from_state: State = from_
        self.to_state: State = to
        self.label: str = label

    def __str__(self):
        """Return the string representation of the transition."""
        if not self.label:
            return f"{self.from_state.id_} --> {self.to_state.id_}"
        return f"{self.from_state.id_} --> {self.to_state.id_} : {self.label}"


class Choice(BaseTransition):
    """Choice class.

    This class represents a choice in a state diagram.

    Attributes:
        from_state (State): The state from which the choice starts.
        to_states (list[State]): The states to which the choice ends.
        conditions (list[str]): The conditions of the choice.
    """

    def __init__(
        self,
        id_: str,
        from_: Optional[State] = None,
        to: Optional[list[State]] = None,
        conditions: Optional[list[str]] = None,
    ) -> None:
        """Initialize a new Choice.

        Args:
            id_ (str): The ID of the choice.
            from_ (Optional[State]): The state from which the choice starts.
            to (Optional[list[State]]): The states to which the choice ends.
            conditions (Optional[list[str]]): The conditions of the choice.
        """
        self.id_: str = text_to_snake_case(id_)
        self.from_state: Optional[State] = from_
        self.to_states: list[State] = to if to is not None else []
        self.conditions: list[str] = conditions if conditions is not None else []

    def __str__(self) -> str:
        """Return the string representation of the choice."""
        string: str = f"state {self.id_} <<choice>>"

        if self.from_state:
            string += f"\n{self.from_state.id_} --> {self.id_}"

        for state in self.to_states:
            string += f"\n{self.id_} --> {state.id_}"
            index = self.to_states.index(state)
            # check if there is a condition for the transition
            if len(self.conditions) > index:
                string += f" : {self.conditions[index]}"

        return string


class Fork(BaseTransition):
    """Fork class.

    This class represents a fork in a state diagram.

    Attributes:
        from_state (State): The state from which the fork starts.
        to_states (list[State]): The states to which the fork ends.
    """

    def __init__(
        self, id_: str, from_: Optional[State] = None, to: Optional[list[State]] = None
    ) -> None:
        """Initialize a new Fork.

        Args:
            id_ (str): The ID of the fork.
            from_ (Optional[State]): The state from which the fork starts.
            to (Optional[list[State]]): The states to which the fork ends.
        """
        self.id_: str = text_to_snake_case(id_)
        self.from_state: Optional[State] = from_
        self.to_states: list[State] = to if to is not None else []

    def __str__(self) -> str:
        """Return the string representation of the fork."""
        string: str = f"state {self.id_} <<fork>>"

        if self.from_state:
            string += f"\n{self.from_state.id_} --> {self.id_}"

        for state in self.to_states:
            string += f"\n{self.id_} --> {state.id_}"

        return string


class Join(BaseTransition):
    """Join class.

    This class represents a join in a state diagram.

    Attributes:
        from_states (list[State]): The states from which the join starts.
        to_state (State): The state to which the join ends.
    """

    def __init__(
        self, id_: str, from_: Optional[list[State]] = None, to: Optional[State] = None
    ) -> None:
        """Initialize a new Join.

        Args:
            id_ (str): The ID of the join.
            from_ (Optional[list[State]]): The states from which the join starts.
            to (Optional[State]): The state to which the join ends.
        """
        self.id_: str = text_to_snake_case(id_)
        self.from_states: list[State] = from_ if from_ is not None else []
        self.to_state: Optional[State] = to

    def __str__(self) -> str:
        """Return the string representation of the join."""
        string: str = f"state {self.id_} <<join>>"

        for state in self.from_states:
            string += f"\n{state.id_} --> {self.id_}"

        if self.to_state:
            string += f"\n{self.id_} --> {self.to_state.id_}"

        return string
