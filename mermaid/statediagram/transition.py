from .state import State, Start, End

class Transition:
    """Transition class.

    This class represents a transition in a state diagram.

    Attributes:
        from_state (State): The state from which the transition starts.
        to_state (State): The state to which the transition ends.
        label (str): The label of the transition.
    """
    def __init__(self, 
                from_: State = Start(), 
                to: State = End(),
                label: str = '') -> None:
        """Initialize a new Transition.

        Args:
            from_ (State): The state from which the transition starts.
            to (State): The state to which the transition ends.
            label (str): The label of the transition.
        """
        self.from_state: State = from_
        self.to_state: State = to
        self.label: str = label

    def __str__(self):
        """Return the string representation of the transition.
        """
        return f'{self.from_state.id_} --> {self.to_state.id_} : {self.label}'